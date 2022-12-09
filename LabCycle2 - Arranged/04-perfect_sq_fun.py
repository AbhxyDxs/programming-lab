import math
def perfect(n,m):
 for i in range(n,m+1):
  c=0.0
  d=0
  if(len(str(i))==4):
       e=even(i)
       if(e):
         c=math.sqrt(i)
         d=int(c)
         if(c==d):
           print(i)
       
def even(j):
 count=0
 while(j>0):
    rem=j%10
    if(rem%2==0):
       count+=1
    j=int(j/10)
 if(count==4):
      return 1
 else:
      return 0

a=int(input("Enter Lower Limit : "))
b=int(input("\nEnter Upper Limit : :"))
perfect(a,b)
