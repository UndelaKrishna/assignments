f=open("krishna.txt","w")
a=open("ram.txt","w")
b=open("virat.txt","w")
c=open("emp.csv","w")

#zipfile
from zipfile import *

f=ZipFile("abcd.zip","w")
f.write("krishna.txt")
f.write("ram.txt")
f.write("virat.txt")
f.write("emp.csv")
f.close()
print("zip file  created")


# #unzip file
from zipfile import *
f=ZipFile("abcd.zip","r")
n=f.namelist()
print(n)
for i in n:
    print("filename=",i)
    #how to read a file
    f1=open(i,"r")
    print(f1.read())
    print()


import os
cwd=os.getcwd()
print("msg",cwd)

# #how to create folder
import os
cwd=os.mkdir("ramu/python")


# # #multiple sub directiories
import os
cwd=os.makedirs("file1/file2/file3/file4")


# #one file in multiple files
import os
os.mkdir("file1/world")
os.mkdir("file1/123")
os.mkdir("file1/hii")
os.mkdir("file1/hello")

os.rmdir("file1/world")#file is empty is deleted

# # how to multiple files deleted--only sub directories deleted
os.removedirs("file1/file2/file3/file4")

import os
print(os.listdir("ramu"))


import os
print(os.listdir("desktop"))

import os
print(os.listdir("."))

import os
print(os.listdir("15-11-23 list datastructures"))









