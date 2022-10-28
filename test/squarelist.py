a=input("Enter Numbers : ")
a=a.split(" ")
b=[]
for i in a:
    b.append(int(i))
print("List of Numbers : ",b)
c=[x*x for x in b]
print("Square of Numbers : ",c)
