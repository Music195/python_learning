import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not
try:
    while True: # The main program loop
        print(' ' * indent, end='') # Print the current indentation
        print('********') # Print the zigzag line
        time.sleep(0.1) # Pause for a moment
        
        if indentIncreasing: # If the indentation is increasing
            indent += 1 # Increase the indentation
            if indent == 20: # If the indentation reaches 20 spaces
                indentIncreasing = False # Change to decreasing
        else: # If the indentation is decreasing
            indent -= 1 # Decrease the indentation
            if indent == 0: # If the indentation reaches 0 spaces
                indentIncreasing = True # Change to increasing
except KeyboardInterrupt: # If the user presses Ctrl-C
     sys.exit() # Exit the program