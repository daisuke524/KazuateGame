# いちばんやさしいPython入門教室
# 4桁の文字を入力できるようにする
# coding:utf-8

import random

#4桁であることをチェックする
isok = False
while isok == False:
    b = input("数を入れてね>")
    if len(b) != 4:
        print("4桁の数字を入力してください")
# 各桁が数字である事を判定する
    else:
        if (b[0] < "0") or (b[0] > "9") :
            print("数字ではありません")
        elif (b[1] < "0") or (b[1] > "9") :
            print("数字ではありません")
        elif (b[2] < "0") or (b[2] > "9") :
            print("数字ではありません")
        elif (b[3] < "0") or (b[3] > "9") :
            print("数字ではありません")
        else:
            isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

