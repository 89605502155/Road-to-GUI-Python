import tkinter as tk
import  subprocess
import sys
import os
from tkinter import *
from button import dd

#h=dd.say_hello()
def f():
    gg=dd()
    print(gg.say_hello())
def add_l():
    gg=dd()
    label=tk.Label(win,text=f'{gg.say_hello()}')
    label.pack()
#def func():
    #win.destroy()
    #p=subprocess.Popen([sys.executable, 'button.py'])
    #print(p.__dict__)
    #os.system('button1.py')
win=tk.Tk()
icon=tk.PhotoImage(file='icon_of_my_application.png')
win.iconphoto(False,icon)
win.title('Ferubko easy learn english')
win.config(bg='green') #В такихже кавычках можно записывать и
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
btn1= tk.Button(win, text='start',
                #command=lambda: func())
               command=add_l  )
#menu_bar = Menu(win)
#win.config(menu = menu_bar)
#menu_bar.add_command(label = "Hello!", command = button.py)
#menu_bar.add_command(label = "Quit", command = button.py)
btn1.pack() 

win.mainloop()
