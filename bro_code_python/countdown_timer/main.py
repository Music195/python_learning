#need to modify the code to work with years and various inputs like months, days, hours, minutes, seconds
import time
import math
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

inputYears = int(input("Enter years: "))
# inputMonths = int(input("Enter months: "))
# inputDays = int(input("Enter days: "))
# inputHours = int(input("Enter hours: "))
# inputMinutes = int(input("Enter minutes: "))
# inputSeconds = int(input("Enter seconds: "))

myRange = inputYears * 365 * 24 * 3600
dayCheck = (myRange // (24 * 3600)) % 365
if dayCheck == 0:
    dayCheck = 365
print(dayCheck)
init = True
n = 0
dec = 0
dayAmount = 0
dayForMonth = 0
i = 0

for x in range(myRange, 0, -86400):
    dec += 1
     #printing the total days
    days = x // (24 * 3600) # // gives the quotient on integer form only 
    year = math.floor (days / 365)
    print (days)
    print(n)
    # checking the month index for the first time only
    #print(init)
    if init:
        if 0 < dayCheck <= 31:
            print("January")
            n = 1
        elif 31 < dayCheck <= 59:
            print("February")
            n = 2
        elif 59 < dayCheck <= 90:
            print("March")
            n = 3
        elif 90 < dayCheck <= 120:
            print("April")
            n = 4
        elif 120 < dayCheck <= 151:
            print("May")
            n = 5
        elif 151 < dayCheck <= 181:
            print("June")
            n = 6
        elif 181 < dayCheck <= 212:
            print("July")
            n = 7
        elif 212 < dayCheck <= 243:
            print("August")
            n = 8
        elif 243 < dayCheck <= 273:
            print("September")
            n = 9
        elif 273 < dayCheck <= 304:
            print("October")
            n = 10
        elif 304 < dayCheck <= 334:
            print("November")
            n = 11
        elif 334 < dayCheck <= 365:
            print("December")
            n = 12
        else:
            n = 0
        init = False
        print(f"n: {n}")
        print()


    print(f"day amount {dayAmount}\n")
    #for checking dec is greater than dayForMonth
    if dec == dayAmount:
        dec = 0
     
    #checking the day amount for each month
    if n in (1,3,5,7,8,10,12):
        dayAmount = 31
        dayForMonth = 31
    elif n in (4,6,9,11):
        dayAmount = 30
        dayForMonth = 30
    elif n == 2:
        #for leap year
        if year % 4 == 0:
            dayAmount = 29
            dayForMonth = 29
        else:
            dayAmount = 28
            dayForMonth = 28
    else:
        dayAmount = 0
        dayForMonth = 0

    #for reducing the days
    dayForMonth -= dec
    print(f"day after decreasement is {dayForMonth}")

    #for decreasing the month
    if dayForMonth == 1:
      n -= 1
      print(f"\nn imediately after decreasement is {n}\n")
      if n == 0:
          n = 12
         
    x = x % (24 * 3600)
    hours = x // 3600
    x %= 3600
    minutes = x // 60
    x %= 60
    seconds = x
    i += 1
    
    if i != myRange // (24 * 3600):
        print(f"\n{year} years, {n} months, {dayForMonth} days, {hours} hours, {minutes} minutes, {seconds} seconds\n")
    else:
        print(f"\n0 years, 0 months, 0 days, 0 hours, 0 minutes\n")
    print(f"final n: {n}")
    print(f"decreasement is {dec}")
    print("-" * 40)

   
    time.sleep(0.1)

print("Time's up!")
