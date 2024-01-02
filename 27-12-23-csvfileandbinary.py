f=open("santa.txt","r")
print(f.tell())
print(f.read(4))

f1=open("beer.jpg",'rb')
f2=open("new1_beer.jpg",'wb')
a=f1.read()
f2.write(a)


f2=open("prabha.mp4",'rb')
f3=open("new_prabha.mp4",'wb')
a=f2.read()
f3.write(a)


import csv
with open("studentrecord.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["student_name","student_rollno","Maths_marks","English marks","Hindi_marks","Science_marks","Social_marks","Total_marks","Average_marks","Percentage","Result"])
    n=int(input("enter number of employee to entry details: "))
    for i in range(1,n+1):
        print(i," STUDENTS MARKS DEATILS ")
        stuname=input("enter name : ")
        sturollno=int(input("enter rollno :"))
        maths=int(input("enter maths marks :"))
        english=int(input("enter english marks : "))
        hindi=int(input("enter hindi marks :"))
        science=int(input("enter science marks :"))
        social=int(input("enter social marks:"))
        a=(maths+english+hindi+science+social)
        total=a
        b=a/5
        Average_marks=b
        x=b/500*100
        per=x
        result="pass" if per>=35 else "fail"
    
        w.writerow([stuname,sturollno,maths,english,hindi,science,social,total,Average_marks,per,result])
    print("totsl emp data written to csv file ")