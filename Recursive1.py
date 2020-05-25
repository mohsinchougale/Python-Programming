#If n= 5, print 5 4 3 2 1 2 3 4 5 using single recursive function

def fact(n):
	
	if(n<1):
		return 0
	else:
		print(n,end=" ")
		fact(n-1)
#Upper two are for 6 to 2		
			
	if(n==1):
		return 0
	else:
		print(n,end=" ")
#In this if else it will start from the innermost fact(1) and go to outermost fact(6)

m=int(input("Enter a number - "))
fact(m)

#Output
#Enter a number - 6
#6 5 4 3 2 1 2 3 4 5 6 


