import pygame as py

class food:
    def __init__(self):
        self.cor = (255, 0, 0)

    def food(self, screen):
        py.draw.rect(screen, self.cor, py.Rect(20, 20, 20, 20))
