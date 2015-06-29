#!/usr/bin/python

###Written by Phuong H. Hoang November 2014###
import pygame
class cl_pygame_setup(object):
    
    def __init__(self):
        pygame.init()

    def display_game(self, mode, caption): # mode is a tuple, caption is a string
        gameDisplay = pygame.display.set_mode(mode)
        pygame.display.set_caption(caption)
        return gameDisplay

    def get_color(self):
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0) 
        green = (0,155, 0)
        blue = (0, 0, 255)
        yellow = (255,255, 0)
        cyan = (0, 255, 255)
        purple = (255, 0, 255)
        return (white, black, red, green,blue, yellow, cyan, purple )
