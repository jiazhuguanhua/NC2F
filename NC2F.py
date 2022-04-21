#!/usr/bin/python3
#2022.4.20---v0.1
#2022.4.21---v1.0
#2022.4.21---v2.0
#SPECIAL THANKS:JingYongming
cnt = 0

def in_get():
    global cnt,typeoutL
    if cnt != 0:
        typeoutL.after(0, typeoutL.destroy)#老师这里我想让typeoutL在1000ms后消失，但是好像不工作啊
    cnt = 1

    cd = typein.get()
    print(cd)
    fd = float(cd)*1.8 +32
    fd = round(fd,1)
    print(fd)
    fdo = "FD: " + str(fd)
    typeoutL = Label(main, text=fdo)
    typeoutL.pack(side=TOP,anchor=W)
    typeoutL.pack()
from tkinter import *
main = Tk()  # 创建窗口对象的背景色
main.title("摄氏转华氏")
typeinL = Label(main, text="摄氏度：")
typeinL.pack(side = TOP,anchor=W)
typeinL.pack()

def _clear():
   typein.delete(0, END)
   if cnt != 0:
        typeoutL.after(2000, typeoutL.destroy)

content = StringVar()
typein = Entry(main,bd =5,textvariable=content)
typein.pack(side = TOP)
typein.pack()

ti_b = Button(main,text='计算')
ti_b.config(command=in_get)
ti_b.pack(side = LEFT,anchor=E)
ti_b.pack()

b_clear = Button(main, text='清空', command=_clear)
b_clear.pack(side = LEFT,anchor=E)
b_clear.pack()

main.mainloop()  # 进入消息循环
