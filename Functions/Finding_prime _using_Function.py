#Write a user defined python function to print all prime numbers within a range

def isprime(n):
	fact=0
	for x in range(1,n):
		if(n%x==0):
			fact+=1
		
	if(fact==1):
		print(n)
		
	
	
	
a=int(input("Enter a lower limit of range - "))
b=int(input("Enter a upper limit of range - "))

for y in range(a,b+1):
	isprime(y)
