from Tkinter import *

from Image  import *
canvas_width = 500

canvas_height = 200

def paint( event ):

   black = "#000000"

   x1, y1 = ( event.x - 1 ), ( event.y - 1 )

   x2, y2 = ( event.x + 1 ), ( event.y + 1 )

   w.create_oval( x1, y1, x2, y2, fill = black )\

def save():
     
   image = w.postscript(file = "image.jpeg", height=100,width=100,colormode="color") 

def clear():

   w.delete("all")   	

c = Tk()

w = Canvas(c, width=canvas_width, height=canvas_height)

B = Button(c, text ="Save", command = save, anchor = N).pack()

B2 = Button(c, text="Clear", command = clear, anchor = N).pack()

w.pack(expand = YES, fill = BOTH)

w.bind( "<B1-Motion>", paint  )
    
mainloop()
