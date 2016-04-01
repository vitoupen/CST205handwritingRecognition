import Tkinter
from Tkinter import *
import tkFont
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename
import pygame
from Drawpad import DrawPad
import Classifier

class IDigit():
	def __init__(self, master, num_neighbors):
	    self.frame = Frame(master, width=200, height=500)
	    self.frame.pack()
	    self.button_frame = Frame(master, width=600, height=100)
	    self.button_frame.pack()
	    
	    self.buildClassifiers(num_neighbors)

	def addButton(self, t, f, fg, bg, afg, abg, c, w, s):
		Button(self.button_frame, text=t, font=f, fg=fg, bg=bg, activeforeground=afg, activebackground=abg, command=c, width=w).pack(side=s)
	
	def buildClassifiers(self, num_neighbors):
	    self.KNN8 = Classifier.initializeClassifier(num_neighbors)
	    #self.KNNM = Classifier.initializeKNNMNISTsmall(num_neighbors)
	
	def classifyButton(self, label):
	    Button(self.frame, text="C\nL\nA\nS\nS\nI\nF\nY", font=tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD), fg="black", bg="#b6b6b6", activeforeground="white", activebackground="#4d4d4d", command=self.classify88, width=2).pack(side=LEFT) 
	    label.pack(side=LEFT)
	    Button(self.frame, text="C\nL\nA\nS\nS\nI\nF\nY", font=tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD), fg="white", bg="#4d4d4d", activeforeground="black", activebackground="#b6b6b6", command=self.classifyMNIST, width=2).pack(side=LEFT) 
	
	def classify88():
	    image = Banana.getSquare(200)
	    # Convert the image to fit the size of the training set ( 8x8 pixels)
	    image.thumbnail((8,8))
	    data = []
	    width = image.width
	    height = image.height
	    pixels = image.load()
	    for w in range(0, width):
	        for h in range(0, height):
	            data.append(pixels[w,h])
	    print clf.predict(data)
	    
	def classifyMNIST():
	    image = Banana.getSquare(200)
	    image.thumbnail((28,28))
	
	def drawpad(self):
		self.pad = DrawPad((300, 300), "white")
		self.pad.draw(10)
		self.setImage(self.pad.getImage())
	#upload the image
	def setImage(self, image=None):
		if (image == None):
		    file_ = askopenfilename()
		    self.image = Image.open(file_)
		else:
			self.image = image
		self.tkimage = ImageTk.PhotoImage(self.image)
		label = Tkinter.Label(self.frame, image=self.tkimage)
		self.classifyButton(label)
		
			
