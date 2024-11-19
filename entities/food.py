import pygame as py
import random #Biblioteca para gerar um número aleatorio em um intervalo

class Food:
    def __init__(self):
        self.cor = (255, 0, 0)
        self.x = random.randint(0, (640 // 20) - 1) * 20 # posição x (posição orizontal) - O chat sugeriu a mult por 20 para alinhas as grades do Thiago
        self.y = random.randint(0, (640 // 20) - 1) * 20 # posição x (posição vertical)
        self.tamanho = 20 

    def food_tela(self, screen):
        py.draw.rect(screen, self.cor, py.Rect(self.x, self.y, self.tamanho, self.tamanho))

    def regenerar_comida(self):
        self.cor = (0,0, 0)
        self.x = random.randint(0, (640 // 20) - 1) * self.tamanho
        self.y = random.randint(0, (640 // 20) - 1) * self.tamanho
        while self.cor == (0, 0, 0):
            self.cor = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            