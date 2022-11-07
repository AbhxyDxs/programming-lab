a=input("Enter A Sentence : ")
a=a.split(" ")
b=[]
for i in a:
	if i not in b:
		b.append(i)
#print(b)

for i in range(0,len(b)):
	print(b[i]," repeats ",a.count(b[i])," times")
