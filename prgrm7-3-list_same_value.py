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

flag=0
for i in int_a:
	for j in int_b:
		if i==j:
			flag=flag+1
			print(i ," present in both lists")
			
if flag==0:
	print("No Common Elements")
