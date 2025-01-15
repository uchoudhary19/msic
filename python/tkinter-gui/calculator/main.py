from tkinter import *

root = Tk(className="Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

Btn_dot = Button(root, text='.', padx=40, pady=20)
Btn_0 = Button(root, text='0', padx=40, pady=20)
Btn_1 = Button(root, text='1', padx=40, pady=20)
Btn_2 = Button(root, text='2', padx=40, pady=20)
Btn_3 = Button(root, text='3', padx=40, pady=20)
Btn_4 = Button(root, text='4', padx=40, pady=20)
Btn_5 = Button(root, text='5', padx=40, pady=20)
Btn_6 = Button(root, text='6', padx=40, pady=20)
Btn_7 = Button(root, text='7', padx=40, pady=20)
Btn_8 = Button(root, text='8', padx=40, pady=20)
Btn_9 = Button(root, text='9', padx=40, pady=20)
Btn_Add = Button(root, text='+', padx=40, pady=20)
Btn_Equals = Button(root, text='=', padx=40, pady=20)
Btn_Sub = Button(root, text='-', padx=40, pady=20)
Btn_Multiple = Button(root, text='x', padx=40, pady=20)
Btn_Divide = Button(root, text='/', padx=40, pady=20)


# put buttons on screen
Btn_0.grid(row=4, column=1)
Btn_dot.grid(row=4, column=2)
Btn_Equals.grid(row=4, column=3)

Btn_1.grid(row=3, column=0)
Btn_2.grid(row=3, column=1)
Btn_3.grid(row=3, column=2)
Btn_Add.grid(row=3, column=3)

Btn_4.grid(row=2, column=0)
Btn_5.grid(row=2, column=1)
Btn_6.grid(row=2, column=2)
Btn_Sub.grid(row=2, column=3)

Btn_7.grid(row=1, column=0)
Btn_8.grid(row=1, column=1)
Btn_9.grid(row=1, column=2)
Btn_Multiple.grid(row=1, column=3)


root.mainloop()