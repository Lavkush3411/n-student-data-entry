from pickle import *
import time
a=1
while a:
    try:
        class student():
            def __init__(self,name,R_n,year):
                self.name=name
                self.R_n=R_n
                self.year=year
            def print_details(self):
                print(f"Name of Student is {self.name} Enrollment no is {self.name} & Studying year is {self.year}")
            @classmethod
            def split(cls,str):
                return cls(*str.split("-"))
        n=int(input("Enter the number of student data u want to add now = "))
        with open("student.txt","wb") as f:
            t=1
            while t:
                try:
                    for i in range(1,n+1):
                        data_student=student.split(input("Enter student details in form of Name-Enrollment-Studying year = "))
                        dump(data_student,f)
                        print(f"Entry of {i} student is done")
                        time.sleep(0.5)
                        t=0
                except:
                    print("ohh u missed something")
                    t=int(input("if u want to add data again press any number otherwise 0 = "))
        with open("student.txt","rb") as f:
            while n>0:
                try:
                    data_student=load(f)
                    data_student.print_details()
                except:
                        print("All student data has been printed")
                        break
        break
    except:
        print("some input is wrongly typed")
        a=int(input("if u want to enter data again enter any number otherwise 0 = "))

