from tkinter import *

root = Tk()
frame1=Frame(root,width=500,heigh=100,bg='green',bd=5)
but=Button(frame1,text=u'Первая кнопка')
var = StringVar()
info = Text(root, width = 40, height = 2, bg = "#597DA3", fg = "white",
               font="Verdana 12",
               wrap=WORD)

but = Button(root,
          text="Next", #надпись на кнопке
          width=10,height=2, #ширина и высота
          bg="#597DA3",fg="white",
          font = 'arial 10') #цвет фона и надписи

info.insert(1.0, "Hello! Do you see this meme?\n If not select New meme or yes select Old meme.")


var1=IntVar()
var2=IntVar()
rbutton1=Radiobutton(root,text='New meme',font = 'arial 10', variable=var,value=1)
rbutton2=Radiobutton(root,text='Old meme', font = 'arial 10', variable=var,value=2)

but.pack(side = "bottom")
rbutton2.pack(side = "bottom", fill = "none")
rbutton1.pack(side = "bottom", fill = "none")
but.pack(side = "bottom")
info.pack(side = "top")
root.title("GoodMems")
root.geometry("700x400")
root.mainloop()
