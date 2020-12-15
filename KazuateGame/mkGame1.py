# いちばんやさしいPython入門教室
# coding:utf-8

import random

# ランダムな1桁の数
a = random.randint(0,9)
# 文字入力をする
b = input("数を入れてね>")
# 当たりかどうか判定する
if a == b:
    print("当たり")
else:
    print("はずれ")
