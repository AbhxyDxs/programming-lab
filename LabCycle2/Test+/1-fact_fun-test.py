def fact_fun():
	a=int(input("Enter A Number : "))
	x=1
	for i in range(1,a+1):
		x=x*i
	print(a,"! =",x)
fact_fun()
