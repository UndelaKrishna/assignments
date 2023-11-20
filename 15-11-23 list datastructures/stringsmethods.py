#strip()
#remove spaces at the begining and at the end of the string
a="     python       "
print(a.strip())



#lstrip()
#remove spaces to the left of the string

n="     jvaadeveloper"
print(n.lstrip())



#rstrip()
#remove any white spaces at the end of the string
r="krishna     "
print(r.rstrip())




#find()
#the find method find the first occurence of the specific value
#find method returns -1 if the value is not found.

f="python is dynamically programming language"
print(f.find("d"))
print(f.find("krishna")) # if the value is not found return (-1)
#Syntax:
# find(substring,start-index,end-index)
print(f.find("p",0,11))
print(f.find("d",0,11))
print(f.find("s",0,5)) #if the value is not found return (-1)



#index()

#the index method find the first occurence of the specific value
#the index method raises an eception if the value is not found

#syntax:
# index(substring,start -index,end -index)

i="java is stattically programming language"
print(len(i))
print(i.index("s"))
print(i.index("p",1,22))
print(i.index("l",1,25))
print(i.index("u",1,25))#if the value is not found



#rfind()
#the rfind method finds the last of occurrence of the specified value
#the r find method returns -1 if the value is not found 

r="python is dynamicall programming language"
print(r.rfind("n"))
#rfind(substring,start-index,end -index)
print(r.rfind("d",1,11))
print(r.find("p",1,27))
print(r.find("p",0,27))
print(r.rfind("t",0,1))#if the value is not found


#rindex()
#the rindex method finds the last of occurrence of the specified value
#the r index method  raise an eception if the value is not found

j="krishnareddy is a developer"
print(len(j))
print(j.rindex("d"))
print(j.rindex("e"))
#syntax:
#rindex(substring,start-index,end -index)

print(r.rindex("d",0,11))
print(j.rindex("y",0,14))
print(r.index("p",1,27))
print(r.rindex("h",0,2))  #  if the value is not found







# all string functions:-


# lower()---to convert upper charcters into lower
# upper()---to convert lower characters to upper
# swapcase()----to convert lower to upper and upper to lower 
# capitalize()--to convert 1st character into upper
# title()---to conver all 1st characters into upper
# startswith()---to check whether the string starts with particular character/word or not
# endswith()----to check whether the string ends with particular character/word or not
# find()---to find the specific element is present or not....if not it will givr -1 as an output
# index()---to find the specific element is present or not....if not it will givr error as an output
# count()---to count how many times particular element is present in a given string(it is case sensitive)
# replace()---to replace the element in a string with some other element
# split()----to split the string based on spaces
# strip()----to remove left side and right side spaces of a string
# rstrip()---only to remove right side spaces
# lstrip()---only to remove left side spaces
# len()----to find the lenght of a string
# join()---to join/add an extra character into the given string
# isalpha()--to check the given string is with alphabets or not
# isdigit()--to check the given string is with digits or not
# isalnum()--to check the given string is with alphabets and digits or not
# islower()---to check the given string is with lower case characters or not 
# isupper()---to check the given string is with upper case characters or not 
# istitle()---to check every 1st character of string is in upper case or not
# isspace()---to check string is only with spaces or not



