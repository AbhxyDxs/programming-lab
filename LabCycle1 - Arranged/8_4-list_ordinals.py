a=input("Enter a String : ")
b=[]
for i in a:
    b.append(i)
print("List of Characters : ",b)
c=[ord(x) for x in b]
print("List of Ordinal Values = ",c)
