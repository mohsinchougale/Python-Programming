#To find nPr (permutations) using while loop

n=int(input("Enter n \n"))
r=int(input("Enter r \n"))
a=1
d=n
while(n>0):
	a*=n
	n-=1
b=1
c=d-r
while(c>0):
	b*=c
	c-=1

ans=int(a/b)
print("The number of permutations =",ans)
	

