# いちばんやさしいPython入門教室
# 入力欄を配置する
# coding:utf-8

import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("数を入力してね")

label1 = tk.Label(root, text="数を入力してね")
label1.place(x = 20, y = 20)

# 入力欄を配置
editbox1 = tk.Entry(width = 4)
editbox1.place(x = 120, y = 20)

root.mainloop()