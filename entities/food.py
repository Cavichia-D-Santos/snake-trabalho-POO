import pygame as py


class Food():
    def __init__(self):
        self.cor = (255, 0, 0)

    def food_screen(self, screen):
        py.draw.rect(screen, self.cor, py.Rect(50, 50, 100, 100))
