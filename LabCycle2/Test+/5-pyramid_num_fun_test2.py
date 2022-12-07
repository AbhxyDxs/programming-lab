def py(n):
 for i in range(1,n+1):
    f=""
    for j in range(1,i+1):
       f+=str(i*j)+" "
    print(f)
b=int(input("\nEnter a no:"))
py(b)