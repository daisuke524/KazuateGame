# いちばんやさしいPython入門教室
# メッシージを表示する
# coding:utf-8

import tkinter as tk 
# messagebox関数をインポート
import tkinter.messagebox as tmsg

# ボタンがクリックされたときの処理
def ButtonClick():
    tmsg.showinfo("テスト", "クリックされたよ")

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

label1 = tk.Label(root, text=("数を入力してね"), font=("Helvetica", 25))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x = 129, y = 60)

button1 = tk.Button(root, text = "クリック", font=("Helvetica", 30), command=ButtonClick)
button1.place(x = 220, y = 60)

root.mainloop()