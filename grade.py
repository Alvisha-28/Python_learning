
#grade processing system
student1 = input("Enter the name of student 1: ")
input_marks = int(input("Enter the marks: "))
marks =[input_marks]
student2 = input("Enter the name of student 2: ")
input_marks = int(input("Enter the marks: "))
marks.append(input_marks)
student3 = input("Enter the name of student 3: ")
input_marks = int(input("Enter the marks: "))
if input_marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
    
elif(input_marks < 0):
        print("Invalid marks. Please enter a value between 0 and 100.") 
elif input_marks <= 100 and input_marks >= 0:
    marks.append(input_marks)
else:
     
    print("Invalid marks. Please enter a value between 0 and 100.")
print("Marks of students: ", marks) 
    
