import time
import math

my_time = int (input("Enter the time in seconds: "))
init = True # initialize init to True

for x in range(my_time, 0, -86400):
    sec = x % 60 # give the remainder when x is divided by 60
    min = int(x / 60) % 60 # give the quotient when x is divided by 60 
                            #and remainder when the quotient is divided by 60
    hr = int(x / 3600) % 24 # give the quotient when x is divided by 3600
    days = math.floor(int(x / 3600) / 24)
    # month_days =math.floor(days % 30) # give the remainder when days is divided by 30
    
    if init:
        check_month = math.floor((int((x/3600)/24) % 365))
        if 0 <= check_month < 31:
            n = 1 # January
        elif 31 <= check_month < 59:
            n = 2 # February
        elif 59 <= check_month < 90:
            n = 3 # March
        elif 90 <= check_month < 120:
            n = 4 # April
        elif 120 <= check_month < 151:
            n = 5 # May
        elif 151 <= check_month < 181:
            n = 6 # June
        elif 181 <= check_month < 212:
            n = 7 # July
        elif 212 <= check_month < 243:
            n = 8 # August
        elif 243 <= check_month < 273:
            n = 9 # September
        elif 273 <= check_month < 304:
            n = 10 # October
        elif 304 <= check_month < 334:
            n = 11 # November
        elif 334 <= check_month <= 365:
            n = 12 # December
        init = False # set init_n to False to exit the loop after the first iteration
    month_days = 0 # initialize month_days to 0
    # Calculate the number of days in the current month
    month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    match month[n-1]:
        case _ if month[n-1] in (1, 3, 5, 7, 8, 10, 12): # months with 31 days
            month_days = math.floor(days % 31) # months with 31 days
            if month_days == 0 and month[n-1] in (1, 3, 5, 7, 8, 10, 12):
                n -= 1 # decrease month if days is 0
        case _ if n in (4, 6, 9, 11): # months with 30 days 
            month_days = math.floor(days % 30) # months with 30 days
            if month_days == 0 and month[n-1] in (4, 6, 9, 11):
                n -= 1 #  decrease month if days is 0      
        case _ if month[n-1] == 2: # February
            month_days = math.floor(days % 28) # February has 28 days in a non-leap year
            if month_days == 0 and month[n-1] == 2:
                n -= 1 #  decrease month if days is 0
        case _:
            month_days = 00 # fallback case, should not happen
    
    print(f"{hr:02} hr: {min:02} min: {sec:02} s : {round(days):03} day/s")
    print(f"{month_days:02} day/s")
    print(f"{month[n-1]} month/s")
    print("{year} year/s".format(year=math.floor((int(x / 3600) / 24)  / 365)))
    print("-" * 35)
    time.sleep(1)
print("Time's up!")