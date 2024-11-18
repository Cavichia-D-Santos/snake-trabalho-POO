import pygame as py
import random #Biblioteca para gerar um número aleatorio em um intervalo

class Food:
    def __init__(self):
        self.cor = (255, 0, 0)
        self.x = random.randint(0, 31) * 20 # posição x (posição orizontal) - O chat sugeriu a mult por 20 para alinhas as grades do Thiago
        self.y = random.randint(0, 31) * 20 # posição x (posição vertical) 

    def food_tela(self, screen):
        py.draw.rect(screen, self.cor, py.Rect(self.x, self.y, 20, 20))

    # def regenerar_comida
