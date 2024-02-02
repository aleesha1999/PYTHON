list1=[]
len1=int(input("Enter the number of  elements  you want to add on list"))
for i in range(0,len1):
     print("Enter the element",i+1)
inp=int(input())
list1.appnd(inp)
s=0
for i in list1:
               s=s+i
print("Sum of elements in list are",s)
            
