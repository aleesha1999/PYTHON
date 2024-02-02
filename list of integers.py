list1=[]
list2=[]
m= int(input("Enter the limit of list1:"))
print("enter the elemements")
for i in range(0,m):
        value=int(input())
        list1.append(value)
n= int(input("Enter the limit of list2:"))
print("enter the elemements")
for i in range(0,n):
        value=int(input())
        list2.append(value)
print(list1,list2)
if len(list1)==len(list2):
      print("Both list1 and  list2 are of the same length")
else:
      print("The sum of both list1 and list2 are  not same length")
if sum(list1)==sum(list2):
      print("The sum of both list1 and list2 are  same")
else:
       print("The sum of both list1 and list2 are  not same")
list3=[each for each in list1 if each in list2]
print("same members  are:",list3)
