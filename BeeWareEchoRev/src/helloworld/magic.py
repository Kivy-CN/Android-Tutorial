
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

Magic("""天下英雄出我辈
一入江湖岁月催""")def Magic(source_text = "", slider_value=1):
    """
    魔法函数，根据 slider_value 的不同进行不同操作
    :param source_text: 输入文本，默认为空字符串
    :param slider_value: 滑块值，默认为1
    :return: None
    """
    result = ''
    if slider_value == 0:
        trans_type = '水平反转'
    elif slider_value == 1:
        trans_type = '垂直反转'
    else:
        trans_type = '传统中文'

    if source_text != '':
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
                            tmp_str = tmp_str +''.join('\u3000')  # 如果是中文，则用空格代替
                        else:
                            tmp_str = tmp_str +''.join('\u0020')  # 如果不是中文，则用空格代替

                        print(tmp_str)


                print(tmp_str)
                if slider_value == 1:
                    pass
                    out_list.append(''.join(tmp_str))
                elif slider_value == 2:
                    out_list.append(''.join(tmp_str)[::-1])  # 如果slider_value为2，则反转输出
                else:
                    pass


            print('原始文本：',raw_list)
            print('\n 输出结果：',out_list)

            rev_list = out_list

        for k in rev_list:
            result= result +''.join(k)+'\n'


        #result= ''.join(rev_list)
        print(result)