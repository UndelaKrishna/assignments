
#pr to enter the name and % of marks in a dict and display info on the screen

student_information={}
no_student=int(input("Enter the number of student: "))
for i in range(no_student):
    name=input("Enter the Name of Student: ")
    percentage=float(int(input("Enter the  student percentage: ")))
    student_information[name]=percentage

print("\nstudent information:")
for name,percentage in student_information.items():
    print(f"{name}:{percentage}%")





