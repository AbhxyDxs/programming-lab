a=input("Enter Numbers : ")
a=a.split(" ")
b=[]
for i in a:
    b.append(int(i))
print("List of Numbers : ",b)
c=[x for x in b if x>0]
print("List of +ve Numbers : ",c)
