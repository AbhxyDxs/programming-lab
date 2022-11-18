def fib_fun():
	n=int(input("Enter Number of terms : "))
	a,b=0,1
	if n<=0:
		print("Invalid Input")
	elif n==1:
		print(" ",a)
	elif n==2:
		print(" ",a,"\n ",b)
	else:
		print(" ",a,"\n ",b)
		for i in range (2,n):
			c=a+b
			a=b
			b=c
			print(" ",c," ")
fib_fun()
