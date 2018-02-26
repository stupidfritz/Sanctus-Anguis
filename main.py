import pygame, sys, random, time
from pygame.locals import *
import pipe, menu
from Button import *
pygame.init()

class Scene:
    scene = "menu"

# create the window
global window, window_width, window_height
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Thingy")

# pipe heights
level = random.randint(50, 450)
level2 = random.randint(50, 450)
level3 = random.randint(50, 450)

# beginning of loop
running = True
clock = pygame.time.Clock()

# position of the 3 pipes
pos1 = 800
pos2 = 800
pos3 = 800


# Pipe spawn points
change = 525
change2 = 525

# The color of the BG
r = 0
g = 150
b = 200
def startt():
    pygame.quit()

# mainloop
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
            
    # Lock the frame rate to 30 fps
    clock.tick(30)

    if Scene.scene == "menu":
        window.fill((0, 0, 0))
        menu.Menu(window=window, size=30, message="Sanctus Anguis",
                    x=315, y=200, color=(255, 255, 255))
        start = Button(text="Begin", rect = (0, 0, 300, 60),
                              bg = (100, 100, 100), fg = (255, 255, 255),
                              bgr = (0, 100, 200), tag = ("menu", None))
        def startt():
            Scene.scene = "game"

        def gone():
            pygame.quit()

        start.Left = 400 - start.Width / 2
        start.Top = (300 - start.Height / 2) + 100
        start.Command = startt

        begone = Button(text = "Quit", rect = (0, 0, 300, 60),
                        bg = (100, 100, 100), fg = (255, 255, 255),
                        bgr = (0, 100, 200), tag = ("menu", None))

        begone.Left = 400 - begone.Width / 2
        begone.Top = (300 - begone.Height / 2) + 210
        begone.Command = gone
        begone.Render(window)
        start.Render(window)
        pygame.display.update()
        
    if Scene.scene == "game":
        
        # fill the BG with the color
        window.fill((r, g, b))


        # position of pipe 
        pos1 -= 4
    
        # the 3 pipes
        pipe.Pipe(window=window, width=40, height=level,
                  color="green", x_start=pos1, y_start=0)
        pipe.Pipe(window=window, width=40, height=level2,
                  color="green", x_start=pos2, y_start=0)
        pipe.Pipe(window=window, width=40, height=level3,
                  color="green", x_start=pos3, y_start=0)

        # pipe spawn loop
        if pos1 <= 1:
            pos1 = 800
        if pos1 == 800:
            level = random.randint(50, 450)
        if pos1 <= change:
            pos2 -= 4
            change += 4
        if pos2 <= change2:
            pos3 -= 4
            change2 += 4
        if pos2 <= 1:
            level2 = random.randint(50, 450)
            pos2 = 800
        if pos3 <= 1:
            pos3 = 800
            level3 = random.randint(50, 350)
        if change >= 800:
            change = 800
        if change2 >= 800:
            change2 = 800
        
   
    # update the display
    pygame.display.update()


# exit the program
pygame.quit()
sys.exit()
