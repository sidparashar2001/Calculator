from tkinter import *
from tkinter import messagebox as mb
from winsound import *



main=Tk()
# configure
main.geometry('360x490')
main.title("Calculator")
main.configure(bg="black")
main.wm_iconbitmap("1.ico")

#functions for calculator

operator=""
play = lambda: PlaySound('Sound.wav', SND_FILENAME)


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func



def fclear():
    global operator
    operator=""
    scr_input.set(operator)

def btn_click(number):
    
    global operator
    operator=operator+str(number)
    scr_input.set(operator)




def fcalculate():
    global operator
    try:
        sumup=str(eval(operator))
    except Exception as e:
        mb.showinfo('Error','Incorrect Input')
        sumup=0
        fclear()
    scr_input.set(sumup)
    operator=""




# Creating calculator
scr_input=StringVar()
txt=Entry(main,font=("Arial",20,"bold"),fg="green",textvariable=scr_input,bd=30,bg="black",justify="right",insertwidth=4)
txt.grid(columnspan=4)

# creating first row of button
b7=Button(main,text="7",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click(7))
b7.grid(row=2,column=0)
b8=Button(main,text="8",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda :btn_click(8))
b8.grid(row=2,column=1)
b9=Button(main,text="9",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda :btn_click(9))
b9.grid(row=2,column=2)
b_plus=Button(main,text="+",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click("+"))
b_plus.grid(row=2,column=3)

# creating second row of button
b4=Button(main,text="4",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click(4))
b4.grid(row=3,column=0)
b5=Button(main,text="5",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda :btn_click(5))
b5.grid(row=3,column=1)
b6=Button(main,text="6",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click(6))
b6.grid(row=3,column=2)
b_minus=Button(main,text="-",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda :btn_click("-"))
b_minus.grid(row=3,column=3)

# creating third row of button
b1=Button(main,text="1",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click(1))
b1.grid(row=4,column=0)
b2=Button(main,text="2",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda :btn_click(2))
b2.grid(row=4,column=1)
b3=Button(main,text="3",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click(3))
b3.grid(row=4,column=2)
b_multiply=Button(main,text="*",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click("*"))
b_multiply.grid(row=4,column=3)

# creating fourth row of button
b0=Button(main,text="0",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda :btn_click(0))
b0.grid(row=5,column=0)
b_clear=Button(main,text="C",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=fclear)
b_clear.grid(row=5,column=1)
b_equal=Button(main,text="=",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=combine_funcs(play, fcalculate))
b_equal.grid(row=5,column=2)
b_div=Button(main,text="/",fg="green",padx=16,pady=16,font=("Arial",20,"bold"),bd=8,bg="black",command=lambda: btn_click("/"))
b_div.grid(row=5,column=3)
main.mainloop()