#Faça um programa que abra e reproduza o audio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('pokemonfirered.mp3')
pygame.mixer.music.play
pygame.event.wait()