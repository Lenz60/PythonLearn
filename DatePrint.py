# import datetime
from datetime import datetime

# Get the current date and time
now = datetime.now()
dateNow = now.date()
dayNow = dateNow.day
monthNow = dateNow.month
yearNow = dateNow.year



# print(now.date().month)
def getBirthDate(date):
    # Get the birth date
    splitted = date.split("/")
    # print(splitted[0])
    return splitted

# dt = "29/07/1999"
# # print(datetime.strptime(dt, '%d/%m/%Y').strftime('%d %B %Y'))
# dtDateTime = datetime.strptime(dt, '%d/%m/%Y')
# # differenciate = now - dtDateTime
# differenciateDate = dateNow - dtDateTime.date()
# differenciateDay = dateNow - dtDateTime.day()
# print(differenciateDay)
# formattedDifferenciate = datetime.strptime(str(differenciate), '%d/%m/%Y').strftime('%d %B %Y')
# print(formattedDifferenciate)
# print(differenciate);

def calculateDate(date):
    # dateArray = getBirthDate(date)
    formattedBirthdate = datetime.strptime(date, '%d/%m/%Y')
    # print(formattedBirthdate.year)
    # print(dateArray)
    # birthDate = int(dateArray[0])
    # birthMonth = int(dateArray[1])
    # birthYear = int(dateArray[2])
    
    thisDay = formattedBirthdate.day - dayNow
    
    formattedDate = formattedBirthdate.strftime('%d %B %Y')
    print("Your birthdate is ", formattedDate )
    sumYear = yearNow - formattedBirthdate.year
    sumMonth = monthNow - formattedBirthdate.month
    sumDay = dayNow - formattedBirthdate.day
    
    if sumMonth <0 :
        sumYear - 1
        sumMonth = 12 + sumMonth
        
    if sumDay < 0:
            sumMonth - 1
            sumDay = 30 + sumDay    
            
    print(f"Your are  {sumYear} year, {sumMonth} month, {sumDay} day years old")
    # print(f"Your are  {yearNow - formattedBirthdate.year} year, {monthNow - formattedBirthdate.month} month, {dayNow - formattedBirthdate.day} day years old")
# print(dt.strftime('%d/%M/%Y'))
