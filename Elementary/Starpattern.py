#To print the followng patterns using for loop take the number of rows from the user
#eg. input is 4. It has odd number of stars starting from 1
# *******
# *****
# ***
# *

n=int(input("Enter the number of rows - "))
a=2*n-1

for x in range(a,0,-2):
	for y in range(1,x+1):
		print('*',end=" ")		
	print("")
