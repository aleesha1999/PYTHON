class student:
  def __init__(self,rollno,name, mark1, mark2):
    self.rollno=rollno
    self.name=name
    self.mark1=mark1
    self.mark2=mark2
  def result(self):
    total= self.mark1+self.mark2
    return total
s=[]
for i  in range(1,4):
 roll=int(input("Enter rollno:"))
 name=input("Enter name:")
 m1=int(input("Enter mark1:"))
 m2=int(input("Enter mark2:"))
 obj=student(roll,name,m1,m2)
 s.append(obj)
t1=s[0].result()
t2=s[1].result()
t3=s[2].result()
print("total mark of student1=",t1)
print("total mark of student1=",t2)
print("total mark of student1=",t3)




