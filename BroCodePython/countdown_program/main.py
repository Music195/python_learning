import time

my_time = int(input("Enter the countdown time in seconds: "))
for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = i // 3600
    print(f"Countdown: {hours:02}:{minutes:02}:{seconds:02} seconds remaining")
    time.sleep(1)


print("Welcome to the Countdown Program!")