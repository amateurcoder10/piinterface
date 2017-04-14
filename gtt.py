from gtts import gTTS
import pygame
import os
tts = gTTS(text='Hello World', lang='en')
tts.save("hello.mp3")


pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
