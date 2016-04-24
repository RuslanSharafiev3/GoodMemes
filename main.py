from Tkinter import *
import random

root = Tk()
info = Text(root, width = 40, height = 2, bg = "#597DA3", fg = "white",
               font="arial 12",
               wrap=WORD)

fra1 = Frame(root,width=500,height=400,bg="#FFFFFF")

but = Button(root,
          text="Next", #надпись на кнопке
          width=10,height=2, #ширина и высота
          bg="#597DA3",fg="white",
          font = 'arial 10') #цвет фона и надписи

info.insert(1.0, "Hello! Do you seen this meme?\n If not select New meme or  yes, then select Old meme.")

counter = 0
def butClick(event):
    random.choice("meme\\")


var1=IntVar()
var2=IntVar()
rbutton1=Radiobutton(root,text='New meme',font = 'arial 10', value=1)
rbutton2=Radiobutton(root,text='Old meme', font = 'arial 10',value=2)


but.pack(side = "bottom")
but.bind('<Button>', butClick)
rbutton2.pack(side = "bottom", fill = "none")
rbutton1.pack(side = "bottom", fill = "none")
but.pack(side="bottom")
fra1.pack(side="bottom")
info.pack(side="top")
root.title("GoodMemes")
root.geometry("800x600")
root.mainloop()
