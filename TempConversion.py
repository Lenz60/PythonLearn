
# ? Celcius to other
def celcius_to_fahrenheit(celcius):
    return celcius * 9/5 + 32

def celcius_to_reamur(celcius):
    return celcius * 4/5

def celcius_to_kelvin(celcius):
    return celcius + 273

# ? Reamur to other
def reamur_to_celcius(reamur):
    return reamur * 5/4

def reamur_to_fahrenheit(reamur):
    return reamur * 9/4 + 32

def reamur_to_kelvin(reamur):
    return reamur * 5/4 + 273

# ? Fahrenheit to other
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_reamur(fahrenheit):
    return (fahrenheit - 32) * 4/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit-32) * 5/9 + 273

# ? Kelvin to other

def kelvin_to_celcius(kelvin):
    return kelvin - 273

def kelvin_to_reamur(kelvin):
    return (kelvin - 273) * 4/5

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273) * 9/5 + 32

def celcius_conversion(choice):
    # decide_conversion(input("Enter your choice : \n"))
    match choice:
        case "1":
            print("Celcius to Fahrenheit")
            celcius = float(input("Enter the celcius value : \n"))
            print("The fahrenheit value is ", celcius_to_fahrenheit(celcius))
        case "2":
            print("Celcius to Reamur")
            celcius = float(input("Enter the celcius value : \n"))
            print("The reamur value is ", celcius_to_reamur(celcius))
        case "3":
            print("Celcius to Kelvin")
            celcius = float(input("Enter the celcius value : \n"))
            print("The kelvin value is ", celcius_to_kelvin(celcius))
        case _:
            print("Invalid choice")
            decide_conversion(input("Enter your choice : \n"))

def reamur_conversion(choice):
    match choice:
        case "1":
            print("Reamur to Celcius")
            reamur = float(input("Enter the reamur value : \n"))
            print("The celcius value is ", reamur_to_celcius(reamur))
        case "2":
            print("Reamur to Fahrenheit")
            reamur = float(input("Enter the reamur value : \n"))
            print("The fahrenheit value is ", reamur_to_fahrenheit(reamur))
        case "3":
            print("Reamur to Kelvin")
            reamur = float(input("Enter the reamur value : \n"))
            print("The kelvin value is ", reamur_to_kelvin(reamur))
        case _:
            print("Invalid choice")
            decide_conversion(input("Enter your choice : \n"))            

def fahrenheit_conversion(choice):
    match choice:
        case "1":
            print("Fahrenheit to Celcius")
            fahrenheit = float(input("Enter the fahrenheit value : \n"))
            print("The celcius value is ", fahrenheit_to_celcius(fahrenheit))
        case "2":
            print("Fahrenheit to Reamur")
            fahrenheit = float(input("Enter the fahrenheit value : \n"))
            print("The reamur value is ", fahrenheit_to_reamur(fahrenheit))
        case "3":
            print("Fahrenheit to Kelvin")
            fahrenheit = float(input("Enter the fahrenheit value : \n"))
            print("The kelvin value is ", fahrenheit_to_kelvin(fahrenheit))
        case _:
            print("Invalid choice")
            decide_conversion(input("Enter your choice : \n"))


def kelvin_conversion(choice):
    match choice:
        case "1":
            print("Kelvin to Celcius")
            kelvin = float(input("Enter the kelvin value : \n"))
            print("The celcius value is ", kelvin_to_celcius(kelvin))
        case "2":
            print("Kelvin to Fahrenheit")
            kelvin = float(input("Enter the kelvin value : \n"))
            print("The fahrenheit value is ", kelvin_to_fahrenheit(kelvin))
        case "3":
            print("Kelvin to Reamur")
            kelvin = float(input("Enter the kelvin value : \n"))
            print("The reamur value is ", kelvin_to_reamur(kelvin))
        case _:
            print("Invalid choice")
            decide_conversion(input("Enter your choice : \n"))

def choice_of_temperatures(choice):
    match choice:
        case "1":
            print("Celcius conversion")
            print("1. Celcius to Fahrenheit")
            print("2. Celcius to Reamur")
            print("3. Celcius to Kelvin")
            celcius_conversion(input("Enter your choice : \n"))
        case "2":
            print("Reamur conversion")
            print("1. Reamur to Fahrenheit")
            print("2. Reamur to Celcius")
            print("3. Reamur to Kelvin")
            reamur_conversion(input("Enter your choice : \n"))
        case "3":
            print("Fahrenheit conversion")
            print("1. Fahrenheit to Celcius")
            print("2. Fahrenheit to Reamur")
            print("3. Fahrenheit to Kelvin")
            fahrenheit_conversion(input("Enter your choice : \n"))
        case "4":
            print("Kelvin conversion")
            print("1. Kelvin to Celcius")
            print("2. Kelvin to Fahrenheit")
            print("3. Kelvin to Reamur")
            kelvin_conversion(input("Enter your choice : \n"))
        case _:
            print("Invalid choice")
            decide_conversion(input("Enter your choice : \n"))            

# ? Conversion choice decision
def decide_conversion(choice):
    match choice:
        case "1":
            print("Celcius to Fahrenheit")
            celcius = float(input("Enter the celcius value : \n"))
            print("The fahrenheit value is ", celcius_to_fahrenheit(celcius))
        case "2":
            print("Celcius to Reamur")
            celcius = float(input("Enter the celcius value : \n"))
            print("The reamur value is ", celcius_to_reamur(celcius))
        case "3":
            print("Celcius to Kelvin")
            celcius = float(input("Enter the celcius value : \n"))
            print("The kelvin value is ", celcius_to_kelvin(celcius))
        case "4":
            print("Fahrenheit to Celcius")
            fahrenheit = float(input("Enter the fahrenheit value : \n"))
            print("The celcius value is ", fahrenheit_to_celcius(fahrenheit))
        case "5":
            print("Fahrenheit to Reamur")
            fahrenheit = float(input("Enter the fahrenheit value : \n"))
            print("The reamur value is ", fahrenheit_to_reamur(fahrenheit))
        case "6":
            print("Fahrenheit to Kelvin")
            fahrenheit = float(input("Enter the fahrenheit value : \n"))
            print("The kelvin value is ", fahrenheit_to_kelvin(fahrenheit))
        case "7":
            print("Reamur to Celcius")
            reamur = float(input("Enter the reamur value : \n"))
            print("The celcius value is ", reamur_to_celcius(reamur))
        case "8":
            print("Reamur to Fahrenheit")
            reamur = float(input("Enter the reamur value : \n"))
            print("The fahrenheit value is ", reamur_to_fahrenheit(reamur))
        case "9":
            print("Reamur to Kelvin")
            reamur = float(input("Enter the reamur value : \n"))
            print("The kelvin value is ", reamur_to_kelvin(reamur))
        case "10":
            print("Kelvin to Celcius")
            kelvin = float(input("Enter the kelvin value : \n"))
            print("The celcius value is ", kelvin_to_celcius(kelvin))
        case "11":
            print("Kelvin to Fahrenheit")
            kelvin = float(input("Enter the kelvin value : \n"))
            print("The fahrenheit value is ", kelvin_to_fahrenheit(kelvin))
        case "12":
            print("Kelvin to Reamur")
            kelvin = float(input("Enter the kelvin value : \n"))
            print("The reamur value is ", kelvin_to_reamur(kelvin))
        case _:
            print("Invalid choice")
            decide_conversion(input("Enter your choice : \n"))
