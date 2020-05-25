s1=input("Enter a string - ")

l=len(s1)
count=0
for x in range(0,l,1):
	if(s1[x]=='a'or s1[x]=='e'or s1[x]=='i'or s1[x]=='o'or s1[x]=='u'):
		count+=1
		
if(count%2==0):
	print("Even")
else:
	print("Odd")
