import tkinter as mod
import time

window = mod.Tk()
window.geometry('350x600')
window.title('Calculator')
window.minsize(350, 600)


def com1():
    entry1.config(state="normal")
    entry1.insert(mod.END, '1')
    entry1.config(state="disabled")


def com2():
    entry1.config(state="normal")
    entry1.insert(mod.END, '2')
    entry1.config(state="disabled")


def com3():
    entry1.config(state="normal")
    entry1.insert(mod.END, '3')
    entry1.config(state="disabled")


def com4():
    entry1.config(state="normal")
    entry1.insert(mod.END, '4')
    entry1.config(state="disabled")


def com5():
    entry1.config(state="normal")
    entry1.insert(mod.END, '5')
    entry1.config(state="disabled")


def com6():
    entry1.config(state="normal")
    entry1.insert(mod.END, '6')
    entry1.config(state="disabled")


def com7():
    entry1.config(state="normal")
    entry1.insert(mod.END, '7')
    entry1.config(state="disabled")


def com8():
    entry1.config(state="normal")
    entry1.insert(mod.END, '8')
    entry1.config(state="disabled")


def com9():
    entry1.config(state="normal")
    entry1.insert(mod.END, '9')
    entry1.config(state="disabled")


def com0():
    entry1.config(state="normal")
    entry1.insert(mod.END, '0')
    entry1.config(state="disabled")


def com_minus():
    entry1.config(state="normal")
    entry1.insert(mod.END, '-')
    entry1.config(state="disabled")


problem_var = mod.StringVar()


def com_equal():
    entry1.config(state="normal")

    solved = eval(entry1.get())
    problem_var.set(solved)

    entry1.config(state="disabled")


def com_multiply():
    entry1.config(state="normal")
    entry1.insert(mod.END, '*')
    entry1.config(state="disabled")


def com_add():
    entry1.config(state="normal")
    entry1.insert(mod.END, '+')
    entry1.config(state="disabled")


def com_decimal():
    entry1.config(state="normal")
    entry1.insert(mod.END, '.')
    entry1.config(state="disabled")

def com_delete():
    entry1.config(state="normal")
    entry1.delete(first=len(entry1.get())-1,last=mod.END)
    entry1.config(state="disabled")

def com_divide():
    entry1.config(state="normal")
    entry1.insert(mod.END, '/')
    entry1.config(state="disabled")

def com_clear():
    entry1.config(state="normal")
    entry1.delete(first=0,last=mod.END)
    entry1.config(state="disabled")


def com_cancel():
    window.destroy()


frame1    = mod.Frame(window)
frame2    = mod.Frame(window)
frame2_2  = mod.Frame(frame2)
frame2_4  = mod.Frame(frame2)
frame2_6  = mod.Frame(frame2)
frame2_8  = mod.Frame(frame2)
frame2_10 = mod.Frame(frame2)
frame10_5 = mod.Frame(frame2_10)

entry1 = mod.Entry(frame1, textvariable=problem_var, font=("Helvetica", 38, "bold"))
entry1.pack(expand=True, fill='both')
entry1.config(state="disabled")

# Other state stuff

delete_button   = mod.Button(frame2_10,text='<', font=("Calibri", 18), width=6, height=2,    command=com_delete)
divide_button   = mod.Button(frame10_5,text='/', font=("Calibri", 18), width=6, height=2,    command=com_divide)
clear_button    = mod.Button(frame10_5,text='C', font=("Calibri", 18), width=6, height=2,    command=com_clear)
button1         = mod.Button(frame2_2, text='1', font=("Calibri", 18), width=6, height=2,    command=com1)
button2         = mod.Button(frame2_2, text='2', font=("Calibri", 18), width=6, height=2,    command=com2)
button3         = mod.Button(frame2_2, text='3', font=("Calibri", 18), width=6, height=2,    command=com3)
add_button      = mod.Button(frame2_2, text='+', font=("Calibri", 18), width=6, height=2,    command=com_add)
button4         = mod.Button(frame2_4, text='4', font=("Calibri", 18), width=6, height=2,    command=com4)
button5         = mod.Button(frame2_4, text='5', font=("Calibri", 18), width=6, height=2,    command=com5)
button6         = mod.Button(frame2_4, text='6', font=("Calibri", 18), width=6, height=2,    command=com6)
minus_button    = mod.Button(frame2_4, text='-', font=("Calibri", 18), width=6, height=2,    command=com_minus)
button7         = mod.Button(frame2_6, text='7', font=("Calibri", 18), width=6, height=2,    command=com7)
button8         = mod.Button(frame2_6, text='8', font=("Calibri", 18), width=6, height=2,    command=com8)
button9         = mod.Button(frame2_6, text='9', font=("Calibri", 18), width=6, height=2,    command=com9)
multiply_button = mod.Button(frame2_6, text='x', font=("Calibri", 18), width=6, height=2,    command=com_multiply)
cancel_button   = mod.Button(frame2_8, text='Quit', font=("Calibri", 18), width=6, height=2, command=com_cancel)
button0         = mod.Button(frame2_8, text='0', font=("Calibri", 18), width=6, height=2,    command=com0)
decimal_button  = mod.Button(frame2_8, text='.', font=("Calibri", 18), width=6, height=2,    command=com_decimal)
equal_button    = mod.Button(frame2_8, text='=', font=("Calibri", 18), width=6, height=2,    command=com_equal, background='lime')

# Pack buttons in frame2
divide_button  .pack(side='right',expand=True, fill='both', padx=3, pady=3)
clear_button   .pack(side='right',expand=True, fill='both', padx=3, pady=3)
delete_button  .pack(side='right',expand=True, fill='both', padx=3, pady=3)
button1        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button2        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button3        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
add_button     .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button4        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button5        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button6        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
minus_button   .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button7        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button8        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
button9        .pack(side='left', expand=True, fill='both', padx=3, pady=3)
multiply_button.pack(side='left', expand=True, fill='both', padx=3, pady=3)
equal_button   .pack(side='right',expand=True, fill='both', padx=2, pady=3)
cancel_button  .pack(side='right',expand=True, fill='both', padx=3, pady=3)
button0        .pack(side='right',expand=True, fill='both', padx=3, pady=3)
decimal_button .pack(side='right',expand=True, fill='both', padx=3, pady=3)

# Pack frames
frame1.place(x=0, y=0, relheight=0.3, relwidth=1)
frame2.place(x=0, rely=0.3, relheight=0.7, relwidth=1)
frame2_6.pack(expand=True, fill='both')
frame2_4.pack(expand=True, fill='both')
frame2_2.pack(expand=True, fill='both')
frame2_8.pack(expand=True, fill='both')
frame2_10.pack(expand=True, fill='both',before=frame2_6)
frame10_5.pack(expand=True, fill='both')

window.mainloop()
