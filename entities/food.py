import pygame as py
import random #Biblioteca para gerar um número aleatorio em um intervalo

class Food:
    def __init__(self):
        self.x = random.randint(0, 31) * 20 #Gera uma posicao x inicial
        self.y = random.randint(0, 31) * 20 #Gera uma posicao y inicial
        self.cor = (255, 0, 0)

    def food_tela(self, screen, consumido):
        if consumido:
            self.x = random.randint(0, 31) * 20  # Nova posicao x
            self.y = random.randint(0, 31) * 20  # Nova posicao y

        py.draw.rect(screen, self.cor, py.Rect(self.x, self.y, 20, 20))


    #def consumida(self, snake):
