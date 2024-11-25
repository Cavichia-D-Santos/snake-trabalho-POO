import pygame as py
import random #Biblioteca para gerar um número aleatorio em um intervalo


class Food:
    def __init__(self):
        self.cor = (255, 0, 0)
        self.x = None
        self.y = None
        self.food_coord()

    def food_coord(self):
        self.x = random.randint(0, 31) * 20  # Nova posicao x
        self.y = random.randint(0, 31) * 20  # Nova posicao y

    def desenhar(self, screen):
        py.draw.rect(screen, self.cor, (self.x, self.y, 20, 20))
