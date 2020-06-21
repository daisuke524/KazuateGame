# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg
from functools import partial
from PIL import Image, ImageTk
import urllib.request as req
import pprint


class Application(tk.Frame):
    def __init__(self, master=None,):
        super().__init__(master)
        self.pack()
        
        #コンピューターのランダム数値 
        self.random = random.randint(1, 4)

        # ラベルを作成
        self.label1 = tk.Label(master, bg = 'SlateGray3', text="ボタン当ててね", font = ('Helvetica', 35), fg='gray45')
        self.label1.place(x = 70, y = 15)

        # 履歴を表示
        self.rirekibox = tk.Text(master, font=("Helvetica", 14), bg = 'SlateGray3', fg='gray45')
        self.rirekibox.place(x=255, y=75, width=90, height=200) 
        

        self.button1 = tk.Button(master, text = ' 1 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'1'))
        self.button1.place(x = 46, y = 74)
        self.button2 = tk.Button(master, text = ' 2 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'2'))
        self.button2.place(x = 150, y = 74)
        self.button3 = tk.Button(master, text = ' 4 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'4'))
        self.button3.place(x = 150, y = 179)
        self.button4 = tk.Button(master, text = ' 3 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'3'))
        self.button4.place(x = 46, y = 179)
    
        self.reset_button = tk.Button(master, text = 'reset', font=('Helvetica',10),fg='gray45',width=48, command=partial(self.reset_action))
        self.reset_button.place(x = 50, y = 290)



    def create_sub_window(self,answer):
    #     # u""" Tk() と同じような感じで使える """
        sub_win = tk.Toplevel(master = self.master)
        sub_win.title(answer)
        c0 = sub_win.Canvas(self, width = 400, height = 350)
        c0.pack()

        image_data = tk.PhotoImage(file = 'test_png')
        c0.create_image(200, 150, image = image_data)






        # sub_win.geometry("300x300")

        # tk.Button(sub_win, text = answer, command = sub_win.destroy).pack()
        # img = Image.open('bg.gif')
        # img = ImageTk.PhotoImage(img)
        # 画像を表示するためのキャンバスの作成（黒で表示）
        # canvas_img = tk.Canvas(sub_win, width=310, height=310 )
        # canvas_img.grid(row=0, column=0)
        # canvas_img.configure(bg='black') # 左上の座標を指定
        # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
        # canvas_img.create_image(0, 0, image=img, anchor=tk.NW)
        
    def click_button(self,num):
        
        # 押下したボタンを判定
        if self.random == int(num):
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "正解 " + "\n" )
            self.create_sub_window('正解')
        elif self.random != int(num):
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "不正解 " + "\n" )
            self.create_sub_window('不正解')

    def reset_action(self):
        self.random = random.randint(1, 4)
        self.rirekibox.delete('1.0', 'end')

    # def image(self):
    #     # 画像を表示するための準備
    #     img = Image.open('omen_hannya.png')
    #     img = ImageTk.PhotoImage(img)
        # 画像を表示するためのキャンバスの作成（黒で表示）
        # canvas = tk.Canvas(bg = "black", width=400, height=300)
        # canvas.place(x=100, y=50) # 左上の座標を指定
        # # # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
        # canvas.create_image(30, 30, image=img, anchor=tk.NW)
        # app.mainloop()


# ウィンドウを作成する
root = tk.Tk()
root.geometry('400x350')
root.title('Random Button')
root.configure(bg='SlateGray3')

app = Application(master=root)
app.mainloop()

