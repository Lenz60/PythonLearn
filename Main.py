import os
import TempConversion as tc;
import DatePrint as dp;
import University as univ;
# # print("Hello world")
# test1 = 1
# test2 = 1.1
# test3 = "1"
# test4 = True
# # ? Casting data
# # data_int = 1;
# # data_float = float(data_int);

# # age = input("Input your age : \n")
# # print (age)
# # print(type(age))
# # print ("Casting age data to float")
# # print(type(float(age)))


# # print(test1)
# # print(test2)
# # print(test3)
# # print(test4)

# # print(type(test1))
# # print(type(test2))
# # print(type(test3))
# # print(type(test4))

# # if(type(test1) == int):
# #     print("This is an integer")
def featureSelect(choice):
    match choice:
        case "1":
            print("Temperature Conversion")
            print("Select what temperature you want to convert")
            print("1. Celcius conversion")
            print("2. Reamur conversion")
            print("3. Fahrenheit conversion")
            print("4. Kelvin conversion")
            choice = input("Enter your choice : \n")
            tc.choice_of_temperatures(choice)
        case "2":
            print("Enter your birthdate")
            date = input("Enter your birthdate in format DD/MM/YYYY : \n")
            dp.calculateDate(date)
        case "3":
            univ.addUniversityData()
        case _:
            print("Invalid choice")
            exit()

# print(chr(27) + "[2J") 
os.system('cls')
InputChoice = input("Select what you want to do : \n1. Temperature Conversion\n2. Date Calculation\n3. Input University Data\n")
featureSelect(InputChoice)

# #  v Temperature Conversion
# # ? Clearing the screen first

# # ? Title
# print("Temperature Conversion")
# print("Select what temperature you want to convert")
# print("1. Celcius conversion")
# print("2. Reamur conversion")
# print("3. Fahrenheit conversion")
# print("4. Kelvin conversion")
# choice = input("Enter your choice : \n")
# # tc.decide_conversion(choice)
# tc.choice_of_temperatures(choice)

# print("Enter your birthdate")
# date = input("Enter your birthdate in format DD/MM/YYYY : \n")
# # dp.getBirthDate(date)
# dp.calculateDate(date)