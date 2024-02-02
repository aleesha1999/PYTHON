string=input("enter a string")
freq=[None]*len(string)
for i  in range(0,len (string)):
    freq[i]=1
    for j in range(i+1, lens(string)):
     if (string[i]==string[j]):
       freq[i]=freq[i]+1
     string=string[j]+'0'+string[j+1]
    print("characters and rheir correspondingfrequencies")
  for i in string(0,len(feq)):  
              if (string[i]!="and string[i]!='0'"):
                print(string[i]+"_"+str(freq[i]))
