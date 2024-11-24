import pygame as py


class points:
    def __init__(self):
        self.pontos = 0
        self.pontos_final = 0
        self.font = py.font.Font("./fontes/PixelDigivolve.otf", 30)

    def pontuacao(self):
        self.pontos += 1

    def total_pontos(self):
        self.pontos_final = self.pontos

    def resetar(self):
        self.pontos = 0

    def desenhar(self, screen):
        pts_tela = self.font.render('Pontos: ' + str(self.pontos), True, (255, 255, 255))
        obj_pontos = self.font.render('/10', True, (255, 255, 255))
        screen.blit(pts_tela, (20, 20))
        screen.blit(obj_pontos, (195, 20))
