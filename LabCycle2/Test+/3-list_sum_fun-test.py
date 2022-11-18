def list_sum_fun():	
	a=input("Enter Numbers : ")
	a=a.split(" ")
	b=[]
	for i in a:
		b.append(int(i))
	print("List Sums to ",sum(b))
list_sum_fun()

