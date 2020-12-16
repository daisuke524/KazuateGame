# いちばんやさしいPython入門教室
# 入力されたテキスト値を取得する
# coding:utf-8

import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
    # テキスト入力欄に入力された文字列を取得
    b = editbox1.get()
    # メッセージとして表示する
    tmsg.showinfo("入力されたテキスト", b)

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

label1 = tk.Label(root, text = "数を入力してね", font=("Helvetica", 25))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font=("Helvetica", 20))
editbox1.place(x = 120, y = 60)

button1 = tk.Button(root, text = "クリック", font=("Helvetica", 30), command=ButtonClick)
button1.place(x = 220, y = 60)

root.mainloop()
