a=input("Enter Elements of A : ")
a=a.split(" ")
int_a=[]
for i in a:
	int_a.append(int(i))
print("List A = ",int_a)

b=input("Enter Elements of B : ")
b=b.split(" ")
int_b=[]
for i in b:
	int_b.append(int(i))
print("List B = ",int_b)

if len(int_a)==len(int_b):
	print("\nLists are of same size")
else:
	print("\nLists are of different size")
