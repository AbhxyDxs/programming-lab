print("Conventional Swapping \n")
a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
print("Before Swap")
print("A=",a," B=",b)
a=a+b
b=a-b
a=a-b
print("After Swap")
print("A=",a," B=",b)

print("\nEz Swapping\n")
e=int(input("Enter 3rd Number : "))
f=int(input("Enter 4th Number : "))
print("Before Swap")
print("E=",e," F=",f)
e,f=f,e
print("After Swap")
print("E=",e," F=",f)
