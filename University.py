import datetime
import os
from ulid import ULID

student_template = {
    "name": "",
    "studentId": 0,
    "curiculum": "",
    "birthdate": datetime.datetime.now(),
}

student_datas = {}

def header():
    os.system('cls')
    print("Welcome to University")
    print(f"{'-'*20}")

def inputAndCheckDate(student):
    
    student["name"] = input("Enter your name : ")
    student["studentId"] = input("Enter your student ID : ")
    student["curiculum"] = input("Enter your curiculum : ")
    while True:
        try:
            YEAR_DATE = int(input("Enter your birth year (YYYY) : "))
            MONTH_DATE = int(input("Enter your birth month (MM) : "))
            DAY_DATE = int(input("Enter your birth day (DD) : "))
            student["birthdate"] = datetime.datetime((YEAR_DATE), (MONTH_DATE), (DAY_DATE))
            break
        except ValueError as e:
            print(f"{e}, Please enter a valid date.")
def setData(student):
    KEY = str(ULID())
    student_datas.update({KEY: student})
    print(f"\n{'ULID':<26} {'Name':<17} {'Student Id':<8} {'Curiculum':<10} {'Birthdate':<10}")
    print(f"{'-'*81}")
    for student in student_datas:
        KEY = student
        
        NAME = student_datas[KEY]["name"]
        STUDENT_ID = student_datas[KEY]["studentId"]
        CURICULUM = student_datas[KEY]["curiculum"]
        BIRTHDATE = student_datas[KEY]["birthdate"].strftime("%d %B %Y")
        
        print(f'{KEY:<3} {NAME:<17} {STUDENT_ID:<8} {CURICULUM:^10} {BIRTHDATE:^20}')
        

def addUniversityData():
    while True:
        header()    
        student = dict.fromkeys(student_template)
        inputAndCheckDate(student)
        setData(student)
        print("\n")  
        is_done = input("Add more data (y/n) : ")
        if is_done == 'n':
            break
    print("Thank you for using this program")