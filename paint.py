from Tkinter import *
from Image  import *

def paint(event):
   black = "#000000"
   x1, y1 = (event.x - 5), (event.y - 5)
   x2, y2 = (event.x + 5), (event.y + 5)
   w.create_oval(x1, y1, x2, y2, fill=black)

def save():
   image = w.postscript(file="image.jpg",
                        height=100, width=100,
                        colormode="color")

def clear():
   w.delete("all")

canvas_width = 500
canvas_height = 500

c = Tk()
message = Label(c, text = "Press & slowly drag the mouse to draw" )
message.pack(side=TOP)
w = Canvas(c, width=canvas_width, height=canvas_height,bg="white")
B = Button(c, text ="Save", command = save, anchor = N).pack(side=LEFT)
B2 = Button(c, text="Clear", command = clear, anchor = N).pack(side=LEFT)
w.pack(expand = YES, fill = BOTH)
w.bind("<B1-Motion>", paint)
    
mainloop()
