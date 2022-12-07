def factor(n):
   for i in range(1,n+1):
       if(n%i==0):
          print(i)
b=int(input("\nEnter a number:"))
print("\n Factors are\n")
factor(b)