class bank:
  def __init__(self,accno,name,accty,bal):
    self.accno=accno
    self.name=name
    self.accty=accty
    self.bal=0
  def showamt(self):
    print("Account holder:",self.accno)
    print("Account name:",self.name)
    print("Account  type:",self.accty)
    print("Your balance amount:",self.bal)
  def depo(self,dl):
    self.bal=self.bal+dl
    return self.bal
  def withd(self,wl):
    self.bal=self.bal-wl
    return self.bal
n=input("Enter your name:")
a=input("enter your accoun number:")
t=input("Enter your account type:")
o=bank(a,n,t,bal=0)
o.showamt()
while(True):
   print("\n Menu")
   print("\n 1.deposit")
   print("\n 2.withdraw")
   c=int(input("Enter your choice:"))
   if(c==1):
    d=int(input("Enter the  amount to deposit"))
    print("you total balance is: ",o.depo(d))
   elif(c==2):
    w=int(input("Enter the amount to be withdrawen:"))
    if(w>d):
     print("insufficent balance")
    else:
     print("you total balance amount is ",o.withd(w))
   else:  
    print("Enter a valid choice")      
          
