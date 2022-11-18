def len_long_word(a):
	b=[]
	a=a.split(" ")
	for i in a:
		b.append(i)
	c=[]
	for i in b:
		c.append(len(i))
	c.sort()
	print("Length of longest word in the list = ",c[-1])


def length_of_longest(words):
	return max([len(word) for word in words])

a=input("Enter A List of Words : ").split()
print(length_of_longest(a))

