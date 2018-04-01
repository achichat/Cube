import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def gen():
    pygame.init()
    width= 800
    height= 600
    screen = (width,height)
    pygame.display.set_mode(screen, GL_DOUBLEBUFFER|OPENGL)
    
    While True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


