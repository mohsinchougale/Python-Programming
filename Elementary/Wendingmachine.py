#Write a python program which simulates a wending machine of your choic. The program must display amenu which consists of three items, each item having a selling price. When the user chooses an item, the machine asks the user to enter the appropriate amount. If the useer enters the amount greater than or equal to the price of the item, the machine dispenses the item and returns the change, otherwise an error message. User can make multiple choices throughout the execution of the program.(Use while loop)

samosacnt=100
samosacost=20
choccnt=100
choccost=10
bisccnt=100
bisccost=15
flag=1
print("Menu:")
print("1. Samosa")
print("2. Chocolates")
print("3. Biscuits")
ch="y"
cost=0
while (ch=="Y" or ch=="y"):
	choice=input("Enter the choice (1/2/3): ")
	choice=int(choice)
	if(choice==1):
		qty=input("Enter quantity: ")
		qty=int(qty)
		if(qty>=0):
			choccnt = choccnt - qty
			if (choccnt<0):
				print("Those many chocolates are not available!")
			elif (choccnt>=0):
				cost = cost + qty*choccost;
	elif(choice==2):
		qty=input("Enter quantity: ")
		qty=int(qty)
		if(qty>=0):
			samosacnt = samosacnt - qty
			if(samosacnt<0):
				print("Those many samosas are not available!")
			elif (samosacnt>=0):
				cost = cost + qty*samosacost;	elif(choice==3):
		qty=input("Enter quantity: ")
		qty=int(qty)
		if(qty>=0):
			bisccnt = bisccnt - qty
			if(bisccnt<0):
				print("Those many biscuits are not available!")
			elif (bisccnt>=0):
				cost = cost + qty*bisccost;
	else:
		print("Wrong choice!")
	ch=input("Do you want to enter more? Enter (y/n): ")
cost=int(cost)
print("Overall order is:")
print("Chocolates:", 100-choccnt)
print("Samosaa:", 100-samosacnt)
print("Biscuits:", 100-bisccnt)
print("Total cost is:", cost)
amt=input("Enter the amount you gave to the vendor: ")
amt=int(amt)
if (cost<=amt):
	print("Pending change to be collected:", amt-cost)
else:
	print("Pending amount to be given:", cost-amt)
