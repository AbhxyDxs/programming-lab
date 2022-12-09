def number_pyramid(n):
	number = 1
	for i in range(1, n+1):
    		for j in range(1, i+1):
        		print(i*j,end=" ")
        		number += 1
    		print()

n=int(input("Enter A Number : "))
number_pyramid(n)
