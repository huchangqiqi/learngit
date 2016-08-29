import os
import re


def find_word(file_path):
    file_list = os.listdir(file_path)
    word_dic = {}
    word_re = re.compile(r'[\w]+')
    for x in file_list:
        if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt':
            try:
                f = open(x,'r')
                data = f.read()
                f.close()
                words = word_re.findall(data)
                for word in words:
                    if word not in word_dic:
                        word_dic[word] =1
                    else:
                        word_dic[word] +=1
            except:
                print('Open %s error' %  x)
    ans_List = sorted(word_dic.items(),key= lambda t:t[1],reverse=True)
    for (key,value) in ans_List:
        print('word',key,'appers %d times'%value)

find_word('.')





