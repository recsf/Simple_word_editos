from tkinter import *
from tkinter import font, filedialog


def save_doc():
    global textarea
    text = textarea.get("1.0", "end-1c")
    location = filedialog.asksaveasfilename()
    file = open(location, "w+")
    file.write(text)
    file.close()


def algerian():
    global textarea
    textarea.config(font="Algerian")


def arial():
    global textarea
    textarea.config(font="Arial")


def courier():
    global textarea
    textarea.config(font="Courier")


def cambria():
    global textarea
    textarea.config(font="Cambria")


def bold_doc():
    global textarea
    textarea.config(font=("arial", 14, "bold"))


root = Tk()
root.title("Notepad")
savebtn = Button(root, command=save_doc, text="Save")
savebtn.grid(row=1, column=0)
savebtn.config(font=("arial", 10, "bold"), fg="black")

fontbtn = Menubutton(root, text="Font")
fontbtn.config(font=("arial", 10, "bold"), fg="black")
fontbtn.grid(row=1, column=1)
fontbtn.menu = Menu(fontbtn, tearoff=0)
fontbtn["menu"] = fontbtn.menu
fontbtn.menu.add_checkbutton(label="Arial", command=arial)
fontbtn.menu.add_checkbutton(label="Algerian", command=algerian)
fontbtn.menu.add_checkbutton(label="Cambria", command=cambria)
fontbtn.menu.add_checkbutton(label="Courier", command=courier)

boldbtn = Button(root, command=bold_doc, text="Bold")
boldbtn.grid(row=1, column=2)
boldbtn.config(font=("arial", 10, "bold"), fg="black")

textarea = Text(root)
textarea.grid(row=2, columnspan=5)

root.mainloop()
