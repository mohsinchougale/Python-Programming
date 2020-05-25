n=int(input("Enter no. of items - "))
menu=[]

for x in range(0,n):
	item=input("Enter name of item - ")
	menu.append(item)
	cost=int(input("Enter cost of item no. - "))
	menu.append(cost)

print(menu)
