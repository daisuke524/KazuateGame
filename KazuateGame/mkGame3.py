# いちばんやさしいPython入門教室
# 4桁のランダムな値を作成
# coding:utf-8

import random

# a1 = random.randint(0,9)
# a2 = random.randint(0,9)
# a3 = random.randint(0,9)
# a4 = random.randint(0,9)

# 上記をリスト化
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))