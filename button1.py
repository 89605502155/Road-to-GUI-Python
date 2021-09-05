import tkinter as tk
import  subprocess
import sys
import os

win=tk.Tk()
icon=tk.PhotoImage(file='icon_of_my_application.png')
win.iconphoto(False,icon)
win.title('Ferubko easy learn english')
win.config(bg='yellow') #В такихже кавычках можно записывать и
# RGB цвета, например какие нибудь оттенки.

label_1=tk.Label(win, text='Ferubko made this',
                 bg='red', fg='yellow', font=('Arial',40,'bold'),
                 padx=19, pady=20,
                 # width и height - ширина и длинна в символах,
                 #а не в пикселях
                 anchor='center', #указывает расположение текста в
                 # прямоугольнике имена=части света на англ и их
                 #м сочетания n=north
                 relief=tk.RAISED,
                 bd=10 # ширина рельефа
                 #justify - выравнивание многострочного текста
                 )
label_1.pack()
btn1= tk.Button(win, text='start'
                )
btn1.pack()

win.mainloop()
