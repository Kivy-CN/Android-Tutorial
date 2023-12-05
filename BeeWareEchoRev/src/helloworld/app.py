"""
My first application
"""
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack
import numpy as np
import pandas as pd 
import matplotlib




def build(app):

    # in_text = toga.TextInput()
    # out_text = toga.TextInput(readonly=True)

    in_text = toga.MultilineTextInput(id='int')
    out_text = toga.MultilineTextInput(id='out')

    in_label = toga.Label("Input", style=Pack(text_align=LEFT))
    out_label = toga.Label("Output", style=Pack(text_align=LEFT))

    box = toga.Box()


    def Trans(widget):
        try:
            out_text.value = Magic(in_text.value)
        except ValueError: 
            out_text.value = "???"

    button = toga.Button("Trans", on_press=Trans)

    box.add(in_label)
    box.add(in_text)
    box.add(out_label)
    box.add(out_text)
    box.add(button)
    

    box.style.update(direction=COLUMN, padding=10)
    

    in_text.style.update(flex=1)
    out_text.style.update(flex=1)
    in_label.style.update(width=100)
    out_label.style.update(width=100)

    button.style.update(padding=15)

    return box



def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def Magic(source_text = "", slider_value=1):
    result = ''
    if slider_value ==0:
        trans_type = 'Horizontal Reverse'
    elif slider_value ==1:
        trans_type = 'Vertical Reverse'
    else:
        trans_type = 'Traditional Chinese'

    if (source_text != ''):
        raw_list = source_text.split('\n')
        #print(raw_list)
        rev_list = []
        out_list = []

        if slider_value == 0:
            for i in raw_list:
                rev_list.append(i[::-1])
            # print(rev_list)
            pass
        else:
            max_lenth=0
            for i in raw_list:
                if len(i)>max_lenth:
                    max_lenth=len(i)


            for i in range(max_lenth):
                tmp_str=''
                for j in raw_list:
                    try:
                        tmp_str = tmp_str +''.join(j[i])

                    except(IndexError):
                        if is_Chinese(raw_list):
                            tmp_str = tmp_str +''.join('\u3000')
                        else:
                            tmp_str = tmp_str +''.join('\u0020')


                        print(tmp_str)


                print(tmp_str)
                if slider_value == 1:
                    pass
                    out_list.append(''.join(tmp_str))
                elif slider_value == 2:
                    out_list.append(''.join(tmp_str)[::-1])
                else:
                    pass


            print('raw is',raw_list)
            print('\n out is',out_list)

            rev_list = out_list

        for k in rev_list:
            result= result +''.join(k)+'\n'


        #result= ''.join(rev_list)
        print(result)
        return(result)


def main():
    return toga.App("Echo Rev", "org.beeware.f_to_c", startup=build)


if __name__ == "__main__":
    main().main_loop()
    