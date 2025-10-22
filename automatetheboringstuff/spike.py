import time, sys
try:
    while True: # The main program loop
        # Draw lines with increasing length
        for i in range(1, 9):
            print("*" * (i * i)) # Print a line with i asterisks
            time.sleep(0.1) # Pause for a moment
        # Draw lines with decreasing length
        for i in range(7, 1, -1):
            print("*" * (i * i)) # Print a line with i asterisks
            time.sleep(0.1) # Pause for a moment
except KeyboardInterrupt: # If the user presses Ctrl-C
    sys.exit() # Exit the program