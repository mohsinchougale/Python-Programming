#Create a second module Testshapes.py which will call the functions in 2DShapes. Make Testshapes menu driven.

import twoDShapes as x

print("Enter y to start")
char=input()


while(char=='y' or char=='Y'):

	print("Which shape do you want?")
	print("1.Circle")
	print("2.Square")
	print("3.Triangle")
	
	n=int(input("Enter the number you want - "))
	
	if(n==1):
		rad=x.read_circle()
		x.area_circle(rad)
	
	elif(n==2):
		side=x.read_square()
		x.area_square(side)
	
	elif(n==3):	
		a,b,c=x.read_triangle()
		x.area_triangle(a,b,c)

	print("Press Y to restart and N to exit")
	char=input()
	




