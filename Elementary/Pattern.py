#To print the followng patterns using for loop take the number of rows from the user
#input is 4, then it will show 4 rows
# 1 3 5 7 5 3 1
#   1 3 5 3 1
#     1 3 1
#       1


n=int(input("Enter the number of rows - "))
a=2*n-1
for r in range(a,0,-2):
	for s in range(0,int((a-r)/2)+1,1):
		print(" ",end=" ")
	for t in range (1,r+1,2):
		print(t,end=" ")
	for u in range (r-2,0,-2):
		print(u,end=" ")
	print()
