import pygame as py
import random

class PathEnemy:
    def __init__(self,):

        self.hitbox = 40 # Tamanho do dano do inimigo
        self.posicoes = ([(0, 0), (0, 0), (0, 0)])
        self.inimigo_Head = self.posicoes[0] # Ponto superior esquerdo do inimigo
        self.proxima_Pos = 1

    def andar(self, posFase, snake): #quant_Pos -> quantas posicoes o inimigo terá na fase
        grid = snake.grid
        prox_x, prox_y = posFase[self.proxima_Pos]
        x, y = self.inimigo_Head
        self.posicoes[0] = posFase[0]

        if x < prox_x:
            x += grid
        elif x > prox_x:
            x -= grid
        if y < prox_y:
            y += grid
        elif y > prox_y:
            y -= grid

        self.inimigo_Head = (x, y)

        if self.inimigo_Head == (prox_x, prox_y):
            self.proxima_Pos += 1
            if self.proxima_Pos >= len(posFase):
                self.proxima_Pos = 0

    def desenhar(self, screen):
        x, y = self.inimigo_Head
        imagem = py.image.load('./entities/inimigos_Sprites/pathEnemy.png')
        imagem_redimensionada = py.transform.scale(imagem, (40, 40))
        screen.blit(imagem_redimensionada, (x, y))