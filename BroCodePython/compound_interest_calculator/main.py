principle = 0
rate = 0
time = 0

while True:
    try:
        principle = float(input("Enter the principle amount: "))
        if principle < 0:
            print("Please enter a positive number for the principle amount.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        rate = float(input("Enter the rate of interest (in %): "))
        if rate < 0:
            print("Please enter a positive number for the rate of interest.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        time = int(input("Enter the time (in years): "))
        if time <= 0:
            print("Please enter a positive number for the time in years.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

total_amount = principle * pow((1 + (rate / 100)), time)

compound_interest = total_amount - principle
print(f"Total amount after {time} years: {total_amount:.2f}")
print(f"Compound interest earned: {compound_interest:.2f}")
# Note: The above code assumes the user will enter valid numeric values for principle, rate, and time.
