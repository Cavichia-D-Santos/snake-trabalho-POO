import pygame as py

class firewall:
    def __init__(self):
        self.hitbox = 40
        self.posicoes = [(120, 520, 300), (120, 500, 300)] # pos. x inicial, pos. x final, pos. y

    def desenhar(self, screen):
        imagem = py.image.load('./entities/imagens_src/firewall.png')
        imagem_redimensionada = py.transform.scale(imagem, (40, 40))

        for pos in range(self.posicoes[0][0], self.posicoes[0][1], 40):
            screen.blit(imagem_redimensionada, (self.posicoes[0][2], pos))
        for pos in range(self.posicoes[1][0], self.posicoes[1][1], 20):
            screen.blit(imagem_redimensionada, (pos, self.posicoes[1][2]))