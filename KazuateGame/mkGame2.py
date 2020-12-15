# いちばんやさしいPython入門教室
# 1桁の数当てゲーム
# coding:utf-8

import random

a = random.randint(0, 9)
print(a)

b = int(input("数を入れてね＞")) # <- 整数に型変換
if a == b:
    print("当たり")
else:
    print("はずれ")


