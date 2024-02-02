n1=int(input("no of elements in the first list:"))
list1=[]
for i in range(n1):
    value=int(input("enter the elements:"))
    list1.append(value)
n2=int(input("Ener  elements in the second list:"))
list2=[]
for i in range(n2):
  value=int(input("Enter no:"))
  list2.append(value)
  if (n1==n2):
    print("Same length")
  else:
   if(sum(list1)==sum(list2)):
     print ("Same sum")
   else:
    list3=[each for each in list1 if each in list2]
    print("same members are:",list3)

            

    
  
