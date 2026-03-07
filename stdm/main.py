# Student management system using CSV files
import csv
#curd create,retrive, update 
 #Features
#1. Add student
#2. View students
#3. Search student
#4. Update student
#5. Delete student

def add_student(id,name, age, grade):
    with open('students.csv', 'a', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow([id,name, age, grade])

def view_students():
    with open('students.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            print(row)

def search_student(id):
    with open('students.csv', 'r') as csvfile:
        r=csv.reader(csvfile) 
        for row in r:
            if row[0] ==id:
              print (row)  
              break
        else:
            print("Student not found")
         
def update_student(id):
    students=[]
    with open('students.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            if row[0] == id:
                print("old details",row)
                name=input("enter your name")
                age=input("enter your age")
                grade=input("enter your grade")
                students.append([id,name, age, grade])
            else:
                students.append(row)

    with open('students.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(students)

def delete_student(id):
    students=[]
    with open('students.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            if row[0] == id:
                
                print("Deleted Details :: ",row)
                continue
            else:
                students.append(row)    
    with open('students.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(students)
    
def menu():
    while True:
        print("1.Add student")
        print("2.View student")
        print("3.Search student")
        print("4.Update student")
        print("5.Delete student")
        choice=int(input("Enter your choice"))

        if choice==1:
            id=input("enter student id")
            name=input("enter your name")
            age=input("enter your age")
            grade=input("enter your grade")
            add_student(id,name, age,grade)
        elif choice==2:
            view_students()
        elif choice== 3:
            id=input("enter student id ::")
            search_student(id)
        elif choice==4:
            id=input("enter student id ::")
            update_student(id)
        elif choice ==5:
            id=input("enter your id ::")
            delete_student(id)  
        else:
            print("Invalid choice") 
            exit()

menu()

