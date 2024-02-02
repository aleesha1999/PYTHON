a=int(input("enter the 1st no in the series"))
b=int(input("enter the 2nd no in the series"))
n= int(input("enter the no:of terms needed"))
print("Fibonacci series")
print(a,b,end= " ")
for i in range(2,n+1):
       f=a+b
       a=b
       b=f
       print(f,end=" ")
