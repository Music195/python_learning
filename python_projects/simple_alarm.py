import os # included environ
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1" # Hide pygame's welcome message
import pygame as pg
import time

second = 0
minute = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
        
def countdown_timer():
    while True:
        input_time = input("Enter the time in seconds: ")
        if input_time.isdigit():
            input_time = int(input_time)
            break
        else:
            print("Invalid input. Please enter a number.")
    time_elapsed = 0  # Local variable - much cleaner!
    while time_elapsed < input_time:
        clear_screen()
        time_elapsed += 1
        time_remaining = input_time - time_elapsed + 1
        print(f"Time left: {time_remaining} seconds")
        time.sleep(1)
    pg.mixer.init()
    pg.mixer.music.load("/home/sawmin/python_learning/python_projects/bird.mp3")
    pg.mixer.music.play()
    input("Alarm sound is playing. Press Enter to stop it.")
    # while pg.mixer.music.get_busy():
    #     pg.time.Clock().tick(10)  # Wait for the music to finish playing
    print("Alarm sound finished playing.")
    
if __name__ == "__main__":
    clear_screen()
    print("Welcome to the Simple Alarm Clock!")
    countdown_timer()
# This is a simple alarm clock that counts down from a specified number of seconds and plays a