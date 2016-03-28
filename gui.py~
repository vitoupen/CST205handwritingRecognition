from Tkinter import *
import Tkinter as tk
import tkFont
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
#==========FUNCTION DEFINITIONS==========
#UPLOAD BUTTON FUNCTION: ALLOWS USER TO SELECT A FILE TO UPLOAD
def browsecsv():
    #Tk().withdraw() #this would prevent the root window from appearing
    filename = askopenfilename() #show an "Open" dialog box and return the path to the selected file
    im = Image.open(filename)
    tkimage = ImageTk.PhotoImage(im)
    tk.Label(master, image=tkimage).pack()
    return filename
#==========STYLE SET UP==========
#? NOT SURE
master = Tk()
#CREATE A CANVAS w SIZE 800x500
w = Canvas(master, width=800, height=500)
#CONTROL WHERE THINGS ARE LOCATED: EXPAND, FILL, SIDES
w.pack()
#SET FONT
courierFont = tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD)
#WINDOW TITLE
master.title("i d i g i t     [Number Identifier]")
#NOTE: TOP FRAME IS DEFAULT
#BOTTOM LOCATION
bottomFrame = Frame(master)
bottomFrame.pack(side = BOTTOM)
#RIGHT LOCATION
rightFrame = Frame(master)
rightFrame.pack(side = RIGHT)
#LEFT LOCATION
leftFrame = Frame(master)
leftFrame.pack(side = LEFT)
#==========BUTTONS==========
"""
BUTTON(LOCATION, TEXT, FONT,
       FOREGROUND(COLOR OF TEXT), BACKGROUND,
       HOVERTEXT, HOVERGROUND)
"""
#BUTTON RESET: CLEARS PROGRAM AND ALLOWS USER TO TRY A NEW PHOTO
resetButton = Button(leftFrame, text="RESET", font=courierFont,
                     fg="black", bg="pink",
                     activeforeground="black", activebackground="red",
                     width = 10)
resetButton.pack(side = LEFT)

#BUTTON UPLOAD: ALLOWS USER TO SELECT A FILE TO UPLOAD
uploadButton = Button(rightFrame, text="UPLOAD", font=courierFont, 
                      fg="black", bg="LightGreen",
                      activeforeground="black", activebackground="LawnGreen",
                      command=browsecsv, width = 10)
uploadButton.pack(side = RIGHT)
#==========PROCESS INPUT HERE==========

#END PROGRAM, RUN IT
mainloop()

"""
import Tkinter as tk

#Creates a window with a quit button that does so when clicked.
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
"""
