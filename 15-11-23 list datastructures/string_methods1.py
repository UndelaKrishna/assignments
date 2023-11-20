
#upper()
#upper method return a string where all character are in uppercase
#symbols and numbers are  ignored
a="HELLOWORLD"
b="python"
c="MY NAME IS KRISHNAREDDY"
d="HIIIhloo"
print(a.upper())
print(b.upper())
print(c.upper())
print(d.upper())


#2).lower():-
#lower method return a string where all character are in lowercase
#symbols and numbers are  ignored


a="KRISHNAREDDY"
b="PYTHON"
c="krishna is a developer"
d="KRISHNA reddy"
print(a.lower())
print(b.lower())
print(c.lower())
print(d.lower())


#3) swapcase():-

#make the lowecase letters upper case and the upper case letters lowercase.
a="Helloworld"
print(a.swapcase())
b="PYTHON"
print(b.swapcase())
c="PYTHON is easy to understand"
print(c.swapcase())
d="krishnareddy"
print(d.swapcase())


#4).# tittle():-
#make the first letter in each word upper case



s="Hello,And Welcome To My World"
print(s.title())

b="hello World"
print(b.title())

c="krishnareddy"
print(c.title())



#5).capitalize():-
#method returns a string where the first  character is upper case,and the rest is lower case

c="hello"
print(c.capitalize())#first letter uppercase incase we can use lowercase output to generate uppercase

d="python is easy to understand"
print(d.capitalize())

e="KRISHNAREDDY"
print(e.capitalize())

f="helloworld"
print(f.capitalize())


#count()
#the count method return the number of times a specified value appers in the string

s="python is very tough and python is logical"
print(s.count("is"))


#replace()

#the replace() method replace a specified pharse with another specified phrase

s="python is very tough and python is logical"
print(s.replace("python","java"))

print(s.replace("sql","java"))


#spilt()

#spilt method spilts a string into a list
#you can specify the separator,default separator is any whitespaes

s="python- is -very- tough- and python= is logical"
print(s.split())
print(s.split(","))
l=s.split("-")
print(l)

s1="python is very tough and python is logical"
l1=s1.split()
for i in l1:
    print(i,end=" ")

print("_________")
#join()
# the join method take all items in an iterable ans joins them into one string
l=["krishna","is","a","developer"]    
# s="#".join(l)
# s="-".join(l)
# s="&".join(l)
s="@".join(l)

print(s)



