def fact_fun(a):
	x=1
	for i in range(1,a+1):
		x=x*i
	print(a,"! =",x)
a=int(input("Enter A Number : "))
fact_fun(a)
