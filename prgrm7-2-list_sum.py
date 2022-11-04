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

print("\nList A sums to ",sum(int_a))
print("\nList B sums to ",sum(int_b))
if sum(int_a)==sum(int_b):
	print("\nLists sums to same value")
else:
	print("\nLists sums to different value\n")
