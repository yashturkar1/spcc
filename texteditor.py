
from Tkinter import *
import tkFileDialog
import tkMessageBox
import datetime
from tkFileDialog import askopenfilename, asksaveasfilename


def normal():

    text.config(font = ("Arial", 10))


def bold():

    text.config(font = ("Arial", 10, "bold"))


def underline():

    text.config(font = ("Arial", 10, "underline"))


def italic():

    text.config(font = ("Arial",10,"italic"))

def opn():

    text.delete(1.0 , END)

    file = open(askopenfilename() , 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT,txt)

    else:

        pass

    

def save():

    filename = asksaveasfilename()

    if filename:

        alltext = text.get(1.0, END)                      

        open(filename, 'w').write(alltext) 



def copy():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get()) 



def paste():

    try:

        txt = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, txt)

    except:

        tkMessageBox.showerror("Error")



def clear():

    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)
    
root = Tk()
root.title("SPCC TEXT EDITOR")
menu = Menu(root)
filemenu = Menu(root)
root.config(menu = menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=opn)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
modmenu = Menu(root)
menu.add_cascade(label="Modify",menu = modmenu)
modmenu.add_command(label="Copy", command = copy)
modmenu.add_command(label="Paste", command=paste)
modmenu.add_separator()
modmenu.add_command(label = "Clear", command = clear)
formatmenu = Menu(menu)
menu.add_cascade(label="Format Menu",menu = formatmenu)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal',command=normal)
formatmenu.add_radiobutton(label='Bold',command=bold)
formatmenu.add_radiobutton(label='Underline',command=underline)
formatmenu.add_radiobutton(label='Italic',command=italic)
text = Text(root, height=30, width=60, font = ("Arial", 10))
scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)                  
text.config(yscrollcommand=scroll.set)           
scroll.pack(side=RIGHT, fill=Y)
text.pack()
root.resizable(0,0)
root.mainloop()
