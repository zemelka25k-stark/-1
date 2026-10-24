from tkinter import *
from tkinter import Tk
root = Tk()
root.title("Olmath_01")

root.geometry("1000x500")
label = Label(root, text = " От олимпиадников и для олимпиадников ", font = "Montserrat")
label.grid(row=0, column=0)

import webbrowser
def open_website():
    webbrowser.open("https://olymp-online.mipt.ru/")
button = Button(root, text="Физтех", command=open_website)
button.grid(row=1, column=0, pady = 20, padx=10)

def open_webite_1():
    webbrowser.open("https://sesc.nsu.ru/olymp-vsesib/")
button1 = Button(root, text="Всесибирская открытая олимпиада школьников", command=open_webite_1)
button1.grid(row=2, column=0,padx=20,pady=10)

root.mainloop()