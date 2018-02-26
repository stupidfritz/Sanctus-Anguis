'''
The example main file for the button.
This is how it will go in
go nuts
- Nathan
'''

import pygame, sys
from Button import *

pygame.init()

# the scene (place in the game)
class Scene:
    scene = "menu"

# the button command
def testt():
    pygame.quit()
    
# create the window
def create_window():
    global window, window_width, window_height
    window_width, window_height = 800, 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Example Thingy")


# initialize BUTTON

btn = Button(text = "YAY", rect = (0, 0, 300, 60),
             bg = (100, 100, 100), fg = (255, 255, 255),
             bgr = (255, 0, 0), tag = ("menu", None))
# button coords
btn.Left = 400 - btn.Width / 2
btn.Top = 300 - btn.Height / 2
# the command of the button
btn.Command = testt

create_window()

# mainloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

        # do the button command when you click the thing
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # detect left click
                # do the thing
                for button in Button.All:
                    if button.Tag[0] == Scene.scene and button.Rolling:
                        if button.Command != None:
                            button.Command() # do the command
                        button.Rolling = False
                        break
    # color the window black
    window.fill((0, 0, 0))
    # render the button to the window
    btn.Render(window)
    # update the display
    pygame.display.update()

# end the program
pygame.quit()
sys.exit()
