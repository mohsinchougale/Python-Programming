#recursive fibonacci

def r_fibo(n):
	if(n==1):
		return 0
	elif(n==2):
		return 1
	else:
		return r_fibo(n-1)+r_fibo(n-2)


def r_print_fib(n):
	if(n>=0):
		fibo=[]
		x=r_fibo(n)
		fibo.append(x)
		return r_print_fib(n-1)




m=int(input("Enter a number - "))
print(r_fibo(m))
d=r_print_fib(m)
print(d.reverse())





