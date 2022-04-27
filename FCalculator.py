from tkinter import *
from tkinter.font import BOLD
from math import *
import random

evaluate=''
def bt_click(item):
    global evaluate
    evaluate=evaluate+str(item)
    ts.set(evaluate)
def math(sign):
    global evaluate
    evaluate=evaluate+str(sign)
    ts.set(evaluate)
def bt_equal():
    global evaluate
    result=eval(evaluate)
    ts.set(result)
    evaluate=''
def clear():
    global evaluate
    evaluate=''
    ts.set('')


    
wn=Tk()
wn.resizable(0,0)
def backgroundcolor():
    colors=['black','brown','purple','green']
    for color in random.choices(colors):
        wn.configure(bg=color)
wn.title('Calculator')
ts=StringVar()
t=Entry(wn, width=50,border=5,font=('arial',20,BOLD),textvariable=ts)
t.grid(row=0,rowspan=1,column=0, columnspan=6)
b1=Button(wn, text='1', width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(1)).grid(row=2,column=0)
b2=Button(wn, text='2', width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(2)).grid(row=2,column=1)
b3=Button(wn, text="3", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(3)).grid(row=2,column=2)
b4=Button(wn, text="4", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(4)).grid(row=3, column=0)
b5=Button(wn, text="5", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(5)).grid(row=3,column=1)
b6=Button(wn, text="6", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(6)).grid(row=3,column=2)
b7=Button(wn, text="7", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(7)).grid(row=4,column=0)
b8=Button(wn, text="8", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(8)).grid(row=4,column=1)
b9=Button(wn, text="9", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(9)).grid(row=4,column=2)
b0=Button(wn, text="0", width=9, height=2, highlightbackground='red',activeforeground='white', highlightthickness=2, command=lambda:bt_click(0)).grid(row=5,column=1)
s1=Button(wn, text="+", width=9, height=2, highlightbackground='orange',activeforeground='white', highlightthickness=2,command=lambda:math('+')).grid(row=4, column=3, pady=5)
s2=Button(wn, text="-", width=9, height=2, highlightbackground='orange',activeforeground='white', highlightthickness=2,command=lambda:math('-')).grid(row=4, column=4, pady=5)
s3=Button(wn, text="X", width=9, height=2, highlightbackground='orange',activeforeground='white', highlightthickness=2,command=lambda:math('*')).grid(row=5, column=3, pady=5)
s4=Button(wn, text='/', width=9, height=2, highlightbackground='orange',activeforeground='white', highlightthickness=2,command=lambda:math('/')).grid(row=5, column=4, pady=5)
s5=Button(wn, text='=', width=18, height=2, highlightbackground='pink',activeforeground='white', highlightthickness=2, command=bt_equal).grid(row=2,column=2,columnspan=4, pady=5)
s6=Button(wn, text='All Clear', width=18, height=2, highlightbackground='pink',activeforeground='white', highlightthickness=2, command=lambda:clear()).grid(row=3,column=2,columnspan=4,pady=5)
s7=Button(wn, text='.',width=9, height=2, highlightbackground='orange',activeforeground='white', highlightthickness=2, command=lambda:math('.')).grid(row=5,column=5,pady=5)
br1=Button(wn, text='(', width=9, height=2, highlightbackground='red', activeforeground='white', highlightthickness=2, command=lambda:bt_click('(')).grid(row=5,column=0)
br2=Button(wn, text=')', width=9, height=2, highlightbackground='red', activeforeground='white', highlightthickness=2, command=lambda:bt_click(')')).grid(row=5,column=2,pady=5)
bb=Button(wn, relief=RIDGE, width=9, height=9, command=backgroundcolor).grid(row=2,column=5,rowspan=3,pady=5)
bs=(Button(wn, text='sin', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('sin'))).grid(row=6,column=0,pady=5)
bc=(Button(wn, text='cos', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('cos'))).grid(row=6,column=1,pady=5)
bt=(Button(wn, text='tan', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('tan'))).grid(row=6,column=2,pady=5)
bs=(Button(wn, text='sec', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('sec'))).grid(row=6,column=3,pady=5)
bco=(Button(wn, text='cosec', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('cosec'))).grid(row=6,column=4,pady=5)
bct=(Button(wn, text='cot', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('cot'))).grid(row=6,column=5,pady=5)
bco=(Button(wn, text='asin', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('asin'))).grid(row=7,column=0)
bco=(Button(wn, text='acos', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('acos'))).grid(row=7,column=1)
bco=(Button(wn, text='atan', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('atan'))).grid(row=7,column=2)
bco=(Button(wn, text='asec', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('asec'))).grid(row=7,column=3)
bco=(Button(wn, text='acosec', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('acosec'))).grid(row=7,column=4)
bco=(Button(wn, text='acot', width=9, height=2, highlightbackground='yellow',activeforeground='white', highlightthickness=2, command=lambda:bt_click('acot'))).grid(row=7,column=5)
wn.mainloop()