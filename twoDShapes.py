#Create a python module called 2DShapes.py. Include functions in the module as following
#1)read circle(read and return radius)
#2)read square(read and return side length)
#3)read triangle(read and return all three sides)
#4)area circle
#5)area square
#6)area triangle

import math

def read_circle():
	radius=float(input("Enter the radius of the circle - "))
	return radius


def read_square():
	side=int(input("Enter the side of the square - "))
	return side
	

def read_triangle():
	a=int(input("Enter the side 1 of the triangle - "))
	b=int(input("Enter the side 2 of the triangle - "))
	c=int(input("Enter the side 3 of the triangle - "))
	return a,b,c
	
def area_circle(radius):
	
	Area= (22/7)*(radius**2)
	print("Area of the circle is ",Area)

def area_square(side):
	
	Area=side*side 	
	print("Area of the square is ",Area)
	
def area_triangle(a,b,c):
	
	semi=(a+b+c)/2
	Area= math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))
	print("Area of the triangle is ",Area)
	
	
	
	
	
	
