import pygame
pygame.mixer.init()
pygame.mixer.music.load("/home/sawmin/python_learning/python_projects/bird.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Wait for the music to finish playing
print("Alarm sound finished playing.")