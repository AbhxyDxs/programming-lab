"""
a=[]
b=[]
a_size=int(input("Enter Number of Elements in A :"))
for i in range(a_size):
	a_el=int(input("Enter Element :"))
	a.append(a_el)
b_size=int(input("Enter Number of Elements in B :"))
for i in range(b_size):
	b_el=int(input("Enter Element :"))
	b.append(b_el)

if len(a)==len(b):
	print("\nLists are of same size")
else:
	print("\nLists are of different size")

"""

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

print("\nList A sums to ",sum(int_a))
print("\nList B sums to ",sum(int_b))
if sum(int_a)==sum(int_b):
	print("\nLists sums to same value")
else:
	print("\nLists sums to different value\n")


for i in int_a:
	for j in int_b:
		if i==j:
			print(i ," present in both lists")
			



