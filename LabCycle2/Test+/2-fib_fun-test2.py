def fib(lim):
	a=0;
	b=1;
	print("\t 0 \n 1");
    
	for i in range(1,lim-1):
		c=a+b;
		print("\t ",c);
		a=b;
		b=c;
fib(int(input("Enter the limit: ")))