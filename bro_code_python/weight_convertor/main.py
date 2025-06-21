weight = float(input("Enter your weight: "))
units = ['kg', 'k', 'lb', 'l']# data type of units is a list, which is a collection of items that can be changed or modified.
print(f"Units available: {', '.join(units)}")   #join the units with a comma and space.
                                                #' '.join() syntax is used to join elements of a list into a string with a specified separator. 
unit = input("Enter the unit (kg/lb or K or L): ").strip().lower() #strip() removes any leading or trailing whitespace, 
                                                                    #and lower() converts the input to lowercase for consistency.




if unit in ['kg', 'k']:
    converted_weight = weight * 2.20462  # Convert kg to lb
    #print(f"{weight} kg is approximately {round(converted_weight, 2)} lb.")
elif unit in ['lb', 'l']:
    converted_weight = weight / 2.20462
    #print(f"{weight} lb is approximately {round(converted_weight, 2)} kg.")
else:
    # print("Invalid unit. Please enter 'kg' or 'lb'.")
    if unit not in units:
        print("Invalid unit. Please enter 'kg' or 'lb'.")
        # exit() 
    

print(f"{weight} {unit} is approximately {round(converted_weight, 2)} {'lb' if unit in ['kg', 'k'] else 'kg'}.")
               