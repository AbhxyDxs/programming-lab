a=input("Enter List Elements : ")
a=a.split(" ")
b=[]
for i in a:
	b.append(int(i))
print("Given List = ",b)
c=[x*x for x in b]
print("Squared List = ",c)
