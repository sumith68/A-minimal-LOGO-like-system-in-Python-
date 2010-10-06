from Tkinter import *
from math import *
c=Canvas(width=400,height=400)
c.pack()
class turtle():
	""" This is the class turtle in which we define two methods forward and rotate to move the turtle in forward direction and for rotating the turtle"""
	def __init__(self,canvas,angle=0,x=200,y=200):
		self.canvas=canvas
		self.angle=angle
		self.x=x
		self.y=y
		self.field=1
		self.hidden=1
		self.p=canvas.create_polygon(215,200,200,195,200,205)
	def forward(self,a):
		if self.field:
			x1=self.x+a*cos((self.angle/180.00)*3.14)
			y1=self.y+a*sin((self.angle/180.00)*3.14)
			
			self.canvas.create_line(self.x,self.y,x1,y1)
			self.x=x1
			self.y=y1
			self.canvas.move(self.p, a * cos((self.angle / 180.00) * 3.14), (a * sin((self.angle / 180.00) * 3.14)))


	def rotate(self,angle):
		self.angle=angle+angle

		self.canvas.delete(self.p)
		x1 = self.x + 15 * cos((self.angle / 180.00) * 3.14)
		y1 = self.y +15 * sin((self.angle / 180.00) * 3.14)
		x2 = self.x + 5 * cos(((90 + self.angle) / 180.00) * 3.14)
		y2 = self.y +5 * sin(((90 + self.angle) / 180.00) * 3.14)
		x3 = self.x + 5 * cos(((270 + self.angle) / 180.00) * 3.14)
		y3 = self.y +5 * sin(((270 + self.angle) / 180.00) * 3.14)
		if self.hidden:
			self.p = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3)

	def hide(self):
		self.hidden=0
	def view(self):
		self.hidden=1
	def penup(self):
		self.field=0
	def pendown(self):
	 	self.field=1
