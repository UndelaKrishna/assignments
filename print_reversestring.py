


#pro to reverse a string s=rangerover is a beast
#ouput = beast a is rangerover
#tsaeb a si revoregnar
#revoregnar si a tsaeb

s="rangerover is a beast"#1).
a=s.split()
for i in a[::-1]:
    print(i,end=" ")     #beast a is rangerover 

print("___________________________________________")
s1="rangerover is a beast" #2).
s1.split()
print(s1[::-1]) # #tsaeb a si revoregnar

print("___________________________________________")

# 3).



# upper()
# lower()  
# swapcase()
# tittle()
# capitalize()

#1).upper():-
a="HELLOWORLD"
b="python"
c="MY NAME IS KRISHNAREDDY"
d="HIIIhloo"
print(a.upper())
print(b.upper())
print(c.upper())
print(d.upper())
print("_____________________________________________________")
#2).lower():-
a="KRISHNAREDDY"
b="PYTHON"
c="krishna is a developer"
d="KRISHNA reddy"
print(a.lower())
print(b.lower())
print(c.lower())
print(d.lower())
print("_____________________________________________________")
#3) swapcase():-
a="Helloworld"
print(a.swapcase())
b="PYTHON"
print(b.swapcase())
c="PYTHON is easy to understand"
print(c.swapcase())
d="krishnareddy"
print(d.swapcase())
print("___________________________________________________________________")
#4).# tittle():-
s="Hello,And Welcome To My World"
print(s.title())

b="hello World"
print(b.title())

c="krishnareddy"
print(c.title())
print("___________________________________________")

#5).capitalize():-
c="hello"
print(c.capitalize())#first letter uppercase incase we can use lowercase output to generate uppercase

d="python is easy to understand"
print(d.capitalize())

e="KRISHNAREDDY"
print(e.capitalize())

f="helloworld"
print(f.capitalize())


  



