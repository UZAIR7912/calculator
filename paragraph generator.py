import tkinter as mod

window = mod.Tk()
window.geometry("450x450")
window.title('paragraph generator')

frame1 = mod.Frame(master = window)
frame2 = mod.Frame(master = window)

def b1():
    label_1.place_forget()
    label_2.place_forget()
    entry_1.place_forget()
    entry_2.place_forget()
    button_1.pack_forget()

    label_3.place(rely=0.35,relx=0.5,anchor='center')
    entry_3.place(rely=0.60,relx=0.5,anchor='center')
    label_4.place(rely=0.35,relx=0.5,anchor='center')
    entry_4.place(rely=0.50,relx=0.5,anchor='center')
    button_2.pack(side='bottom',pady=5)

def generate():
    label_3.place_forget()
    entry_3.place_forget()
    label_4.place_forget()
    entry_4.place_forget()
    button_2.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    paragraph.pack()

label_1  = mod.Label(frame1,text="What is your full name?")

entry_1  = mod.Entry(frame1)
text1 =mod.StringVar(entry_1)
entry_8  = mod.Entry(frame1,textvariable=text1)
entry_1 = entry_8

label_2  = mod.Label(frame2,text="what is your age?")

entry_2  = mod.Entry(frame2)
text2 = mod.StringVar(entry_2)
entry_7  = mod.Entry(frame2,textvariable=text2)
entry_2 = entry_7

button_1 = mod.Button(window,text="Next",width=10,height=1,font=('calibri',12,'bold'),command=b1)


label_3  = mod.Label(frame1,text="What is your favorite book?")

entry_3  = mod.Entry(frame1)
text3 =mod.StringVar(entry_3)
entry_6  = mod.Entry(frame1,textvariable=text3)
entry_4 = entry_6


label_4  = mod.Label(frame2,text="what is your favourite animal?")

entry_4  = mod.Entry(frame2)
text4 =mod.StringVar(entry_4)
entry_5  = mod.Entry(frame2,textvariable=text4)
entry_4 = entry_5

button_2 = mod.Button(window,text="Generate Paragraph!",width=20,height=1,font=('calibri',12,'bold'),command=generate)

paragraph= mod.Label(window,text=f'''
hi {text1},i am an AI used to generate
a paragraph for kids,it looks like your age
is {text2}. I was shocked when i came to know
that your favourite book is {text3}!!!.I have 
read that book before , it was very interesting!
And your favourite animal, {text4} is not a bad opinion. 
by the way this all that i can generate , bye bye!!!''')

label_1.place(rely=0.35,relx=0.5,anchor='center')
entry_1.place(rely=0.60,relx=0.5,anchor='center')
label_2.place(rely=0.35,relx=0.5,anchor='center')
entry_2.place(rely=0.50,relx=0.5,anchor='center')
button_1.pack(side='bottom',pady=5)

frame1.pack(expand=True, fill='both')
frame2.pack(expand=True, fill='both')

window.mainloop ()