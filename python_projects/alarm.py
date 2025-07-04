import time
import datetime
import subprocess
import os
import pygame

def play_alarm_sound():
    """Play alarm sound using pygame"""
    try:
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Try to play the MP3 file using pygame
        if os.path.exists('alarm_sound.mp3'):
            try:
                pygame.mixer.music.load('alarm_sound.mp3')
                pygame.mixer.music.play()
                print("🔊 Playing alarm sound with pygame...")
                
                # Wait for the sound to finish playing
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                return
                
            except pygame.error as e:
                print(f"Pygame error: {e}")
                # Fall back to system players
                pass
        
        # Fallback: Try system audio players
        if os.path.exists('alarm_sound.mp3'):
            # Try different players available on Linux
            players = ['mpg123', 'mplayer', 'vlc', 'ffplay']
            for player in players:
                try:
                    subprocess.run([player, 'alarm_sound.mp3'], 
                                 check=True, 
                                 stdout=subprocess.DEVNULL, 
                                 stderr=subprocess.DEVNULL)
                    print("🔊 Playing alarm sound with system player...")
                    return
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
        
        # Final fallback: system beep
        print("🔔 Audio file not found or players unavailable, using system beep...")
        for i in range(5):
            print('\a', end='', flush=True)  # System beep
            time.sleep(0.5)
                
    except ImportError:
        print("🔔 Pygame not available, using system beep...")
        for i in range(5):
            print('\a', end='', flush=True)
            time.sleep(0.5)
    except Exception as e:
        print(f"Error playing sound: {e}")
        print("🔔 Using system beep as fallback...")
        for i in range(5):
            print('\a', end='', flush=True)
            time.sleep(0.5)

def set_alarm():
    """Set an alarm for a specific time"""
    print("⏰ Simple Alarm Clock")
    print("=" * 30)
    
    try:
        # Get alarm time from user
        alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        
        # Validate time
        if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
            print("❌ Invalid time format!")
            return
            
        # Create alarm datetime object
        now = datetime.datetime.now()
        alarm_datetime = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
        
        # If alarm time is in the past, set it for tomorrow
        if alarm_datetime <= now:
            alarm_datetime += datetime.timedelta(days=1)
            
        print(f"⏰ Alarm set for: {alarm_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print("💤 Waiting for alarm time...")
        
        # Wait until alarm time
        while datetime.datetime.now() < alarm_datetime:
            time.sleep(1)
            
        # Trigger alarm
        print("\n🚨 ALARM! WAKE UP! 🚨")
        play_alarm_sound()
        
    except ValueError:
        print("❌ Invalid time format! Please use HH:MM format.")
    except KeyboardInterrupt:
        print("\n⏹️ Alarm cancelled.")

def countdown_timer():
    """Set a countdown timer"""
    print("⏱️ Countdown Timer")
    print("=" * 30)
    
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        total_seconds = minutes * 60 + seconds
        
        if total_seconds <= 0:
            print("❌ Invalid time!")
            return
            
        print(f"⏱️ Timer set for {minutes} minutes and {seconds} seconds")
        print("⏳ Countdown started...")
        
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            print(f"\r⏱️ Time remaining: {mins:02d}:{secs:02d}", end='', flush=True)
            time.sleep(1)
            total_seconds -= 1
            
        print("\n🔔 Time's up!")
        play_alarm_sound()
        
    except ValueError:
        print("❌ Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n⏹️ Timer cancelled.")

def main():
    """Main menu"""
    while True:
        print("\n⏰ Alarm & Timer App")
        print("=" * 30)
        print("1. Set Alarm")
        print("2. Countdown Timer")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            set_alarm()
        elif choice == '2':
            countdown_timer()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()