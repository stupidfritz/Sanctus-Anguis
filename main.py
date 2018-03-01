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
pygame.display.set_caption("Sanctus Anguis")

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

# FUNCTIONS FOR BUTTONS
def ps():
    pygame.mixer.music.load("smash.mp3")
    pygame.mixer.music.play(-1, 0.0)
    time.sleep(0.5)
    pygame.mixer.music.stop()
    
def startt():
    ps()
    Scene.scene = "game"

def gone():
    pygame.quit()

def poos():
    Scene.scene = "pause"

def bacc():
    Scene.scene = "menu"
# INITAILIZE GUI

# The begin Button
start = Button(text="Begin", rect = (0, 0, 300, 60),
               bg = (100, 100, 100), fg = (255, 255, 255),
               bgr = (0, 100, 200), tag = ("menu", None))
        
start.Left = 400 - start.Width / 2
start.Top = (300 - start.Height / 2) + 100
start.Command = startt

# The Quit Button
begone = Button(text = "Quit", rect = (0, 0, 300, 60),
                bg = (100, 100, 100), fg = (255, 255, 255),
                bgr = (0, 100, 200), tag = ("menu", None))

begone.Left = 400 - begone.Width / 2
begone.Top = start.Top + 5 + begone.Height
begone.Command = gone

# The Pause Button
pause = Button(text = "Pause", rect = (0, 0, 150, 60),
               bg = (100, 100, 100), fg = (255, 255, 255),
               bgr = (0, 100, 200), tag = ("game", None))

pause.Left = 800 - pause.Width
pause.Top = 0
pause.Command = poos

#The resume Button
resume = Button(text = "Resume", rect = (0, 0, 150, 60),
                bg = (100, 100, 100), fg = (255, 255, 255),
                bgr = (0, 100, 200), tag = ("pause", None))

resume.Left = 400 - (resume.Width / 2)
resume.Top = 250
resume.Command = startt

# THE BACK BUTTON
OSA = Button(text = "Menu", rect = (0, 0, 150, 60),
             bg = (100, 100, 100), fg = (255, 255, 255),
             bgr = (0, 100, 200), tag = ("pause", None))
OSA.Left = 400 - (OSA.Width / 2)
OSA.Top = resume.Top + 5 + OSA.Height
OSA.Command = bacc


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
        window.fill((0, 0, 70))
        menu.Menu(window=window, size=30, message="Sanctus Anguis",
                  x=295, y=200, color=(255, 255, 255))
        
        begone.Render(window)
        start.Render(window)

        
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

        pause.Render(window)
            
    if Scene.scene == "pause":

        resume.Render(window)
        OSA.Render(window)

        
    # update the display
    pygame.display.update()


# exit the program
pygame.quit()
sys.exit()
