import customtkinter as mod

def command():
    kg_input = entry_int.get()
    grams_output = kg_input * 1000
    output_str.set(str(grams_output) + str(' grams'))
def cancel():
    window.destroy()

window = mod.CTk()
window.title('weight converter')
window.geometry('300x150')

label1 = mod.CTkLabel(window, text="kg to grams", font=('calibri 24 bold', 25))
label1.pack()

input_frame = mod.CTkFrame(window)

button = mod.CTkButton(input_frame, text='convert', fg_color='red', font=('calibri 12 bold', 25), command = command)
button2 = mod.CTkButton(window, text ='quit',fg_color='white',width =32,height = 16,text_color = 'black',command = cancel)
button2.place(x=250, y=125)

entry_int = mod.IntVar()

entry = mod.CTkEntry(input_frame, textvariable = entry_int)
entry.pack(side = 'left', padx = 10)

button.pack(side = 'left', padx = 10)
input_frame.pack()

output_str = mod.StringVar()
output = mod.CTkLabel(window, text='output', font=('calibri 24', 25), textvariable = output_str)
output.pack(pady = 5)

window.mainloop()