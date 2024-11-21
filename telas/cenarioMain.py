import pygame as py
import pygame.image
from entities import points


class tela:# Caracteristicas da tela e da grid
    def __init__(self, alturaTela, larguraTela):
        self.larguraTela = larguraTela
        self.alturaTela = alturaTela
        self.screen = py.display.set_mode((self.alturaTela, self.larguraTela))
        py.display.set_caption("Snake.exe")  # Nome da página

    def tela_jogo(self): # Funcao a ser chamada no loop
        fundoCor = (0, 0, 0)
        linhasFundo = (0, 100, 0)
        tamanhoGrid = 20
        self.screen.fill(fundoCor)

        for x in range(tamanhoGrid, self.larguraTela, tamanhoGrid):
            py.draw.line(self.screen, linhasFundo, (x, 0), (x, self.alturaTela))
        for y in range(tamanhoGrid, self.alturaTela, tamanhoGrid):
            py.draw.line(self.screen, linhasFundo, (0, y), (self.larguraTela, y))

    def tela_fim_jogo(self): # Ainda vou modificar, deixado apenas para teste
        imagem = pygame.image.load('tela-game-over.png')
        fonte = 'Gameplay.ttf'
        verde = (0, 100, 0)
        font = py.font.Font(fonte, 50)
        medium_font = py.font.Font(fonte, 25)
        small_font = py.font.Font(fonte, 20)
        self.screen.blit(imagem, (141, 161), (131, 131, 419, 319))

        game_over = font.render("Game Over", True, (0, 100, 0))
        pontuacao = medium_font.render(f'Pontos: {points.points().pontos}', True, verde) # FAZER OS PONTOS APARECEREM CORRETAMENTE
        reiniciar = small_font.render('Reiniciar (R)', True, verde)
        quitar = small_font.render('Sair (Q)', True, verde)

        self.screen.blit(game_over, (160, 175))
        self.screen.blit(pontuacao, (245, 300))
        self.screen.blit(reiniciar, (165, 435))
        self.screen.blit(quitar, (380, 435))
