# いちばんやさしいPython入門教室
# ウィンドウにメッセージの位置を決めて表示する
#  coding:utf8

import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

# ウィンドウにメッセージを表示させる
label1 = tk.Label(root, text="数を入力してね")
label1.place(x = 20, y = 20)

root.mainloop()