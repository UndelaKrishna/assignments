#read
f=open("d1.txt","r")
print(f.read())

f=open("d1.txt","r")
print(f.read(10))

#write
f1=open("ball.txt","w")
print(f1.write("hii this is krishna reddy"))

#append
f=open('a2.txt',"a")
print(f.write("python is dynamically language")) 

#r+
f=open("r1.txt","r+")
print(f.read())

#w+
f=open("w1.txt","w+")
print(f.write("python programming"))

#r+w+
f1=open("rw1.txt","r+")
print(f1.write("helloworld"))

#a+
f1=open("append1.txt","a+")
print(f1.write("helloworld"))

#x
f2=open("myfile.txt","x")

 


