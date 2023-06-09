import pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client Side")

client_number = 0

class Player():
    def __init__ (self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height) 

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)        

    def move(self):
        pygame.key.get_pressed()


def redraw_window():
    win.fill(255,255,255,255)
    pygame.display.update()

def main():
    run = True

    for event in pygame:
        if event.type == pygame.QUIT:
            run = False
            pygame.quit

    redraw_window()

