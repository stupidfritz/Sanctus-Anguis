import pygame

pygame.init()

# detect the mouse being over the button
def MouseOver(rect):
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > rect[0] and mouse_pos[0] < rect[0] + rect[2] and mouse_pos[1] > rect[1] and mouse_pos[1] < rect[1] + rect[3]:
        return True
    else:
        return False

        
class Button:

    All = []
    Default = pygame.font.SysFont("Verdana", 20)
    def __init__(self, text, rect, bg, fg, bgr, font = Default, tag = ("menu", None)):
        self.Text = text
        self.Left = rect[0]
        self.Top = rect[1]
        self.Width = rect[2]
        self.Height = rect[3]
        self.Command = None
        self.Rolling = False
        self.Tag = tag

        # NORMAL BUTTON
        self.Normal = pygame.Surface((self.Width, self.Height), pygame.HWSURFACE|pygame.SRCALPHA)
        self.Normal.fill(bg)
        RText = font.render(text, True, fg)   # text, antialiasing, color
        txt_rect = RText.get_rect()
        self.Normal.blit(RText, (self.Width / 2 - txt_rect[2] / 2, self.Height / 2 - txt_rect[3] / 2))

        # HIGHLIGHTED BUTTON
        self.High = pygame.Surface((self.Width, self.Height), pygame.HWSURFACE|pygame.SRCALPHA)
        self.High.fill(bgr)
        self.High.blit(RText, (self.Width / 2 - txt_rect[2] / 2, self.Height / 2 - txt_rect[3] / 2))

        # SAVE BUTTON
        Button.All.append(self)

    # render the button
    def Render(self, to, pos = (0, 0)):
        if MouseOver((self.Left + pos[0], self.Top + pos[1], self.Width, self.Height)):
            to.blit(self.High, (self.Left + pos[0], self.Top + pos[1]))
            self.Rolling = True
        else:
            to.blit(self.Normal, (self.Left + pos[0], self.Top + pos[1]))
            self.Rolling = False

    
