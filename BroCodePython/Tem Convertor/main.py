# Continuously prompt the user until a valid unit is entered
while True:
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
    if unit.lower() in ["c", "f"]:
        break
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# try:
#     tem = float(input("Enter the temperature: "))
# except ValueError:
#     print("Invalid temperature. Please enter a numeric value.")
#     exit()

while True:
    try:
        tem = float(input("Enter the temperature: "))
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if unit.lower() == "c":
    tem = round((tem * 9/5) + 32, 2)
else:
    tem = round((tem -32) * 5/9, 2)
# elif unit.lower() == "f":
#     tem = round((tem -32) * 5/9, 2)
# else:
#     print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
#     exit()

print(f"The converted temperature is: {tem} °{'F' if unit.lower() == 'c' else 'C'}")


