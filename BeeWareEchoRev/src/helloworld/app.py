"""
My first application
"""
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack
import numpy as np
import pandas as pd 
import matplotlib




def build(app):
    # 创建一个文本输入框和一个只读的文本输入框
    # in_text = toga.TextInput()
    # out_text = toga.TextInput(readonly=True)
    
    # 创建一个多行文本输入框和一个只读的多行文本输入框，并给它们分别设置id属性
    in_text = toga.MultilineTextInput(id='int')
    out_text = toga.MultilineTextInput(id='out')

    # 创建一个标签组件用于显示输入框的标签和输出框的标签
    in_label = toga.Label("Input", style=Pack(text_align=LEFT))
    out_label = toga.Label("Output", style=Pack(text_align=LEFT))

    # 创建一个容器组件
    box = toga.Box()

    # 定义一个内部函数，用于将输入框的值经过Magic函数处理后赋值给输出框的值
    def Trans(widget):
        try:
            out_text.value = Magic(in_text.value)
        except ValueError:
            out_text.value = "???"

    # 创建一个按钮组件，并将内部函数Trans设置为点击按钮后的操作
    button = toga.Button("Trans", on_press=Trans)

    # 将各个组件添加到容器组件中
    box.add(in_label)
    box.add(in_text)
    box.add(out_label)
    box.add(out_text)
    box.add(button)

    # 设置容器组件的样式
    box.style.update(direction=COLUMN, padding=10)

    # 设置输入框和输出框的样式
    in_text.style.update(flex=1)
    out_text.style.update(flex=1)
    in_label.style.update(width=100)
    out_label.style.update(width=100)

    # 设置按钮的样式
    button.style.update(padding=15)

    # 返回容器组件
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
    