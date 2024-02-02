word=input("Enter the word :")
vowels=['a','e','i','o,''u' ,'A','E','I','O','U']
wordvowels=[]
for x in word:
    if(x in vowels and x not in wordvowels):
        wordvowels.append(x)
print("vowels in ",word,"are:",wordvowels)




       






        
