from tkinter import *


root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Name: ")

def e_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()
    
my_button = Button(root, text="mash here", command=e_click)
my_button.pack()


root.mainloop()