#1).
s1="example"
vowels=set('aeiouAEIOU') #INTIALIZATION
#Finding unique vowels
count=0
v1=vowels.union(set(s1))
v2=v1.intersection(vowels)

#iterate through the unique vowels set and each vowel
for vowel in  v2:
    print(vowel,end=" ")
    count=count+1
print("total count=",count)


# #2).
s1="example"
s2="aeiouAEIOU"
count=0
vowels=set(s1)
print(vowels)

vowels1=set(s2)
print(vowels1)
#finding vowels
v1=vowels1.union(set(s1))
#printing vowels                                                            
for i in s2:
    print(i,end=" ")
    count=count+1
print("total count=",count)    



#3).

s1="example"
vowels=set('aeiouAEIOU') #INTIALIZATION
#Finding unique vowels
count=0
v1=vowels.union(set(s1))
#printing vowels
for vowel in  v1:
    if vowel in vowels:
             print(vowel,end =" ")
             count=count+1
print("total count=",count)

