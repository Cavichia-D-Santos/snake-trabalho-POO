import pygame as py
import pygame.image


class tela:  # Características da tela e da grid
    def __init__(self, altura_tela, largura_tela, points):
        self.larguraTela = largura_tela
        self.alturaTela = altura_tela
        self.screen = py.display.set_mode((self.alturaTela, self.larguraTela))
        self.points = points  # Referência ao objeto points
        py.display.set_caption("Snake.exe")  # Nome da página

    def tela_jogo(self):
        fundo_cor = (0, 0, 0)
        linhas_fundo = (0, 100, 0)
        tamanho_grid = 20
        self.screen.fill(fundo_cor)

        for x in range(tamanho_grid, self.larguraTela, tamanho_grid):
            py.draw.line(self.screen, linhas_fundo, (x, 0), (x, self.alturaTela))
        for y in range(tamanho_grid, self.alturaTela, tamanho_grid):
            py.draw.line(self.screen, linhas_fundo, (0, y), (self.larguraTela, y))

    def tela_fim_jogo(self):
        imagem = pygame.image.load('./telas/tela-game-over.png')
        fonte = './fontes/Gameplay.ttf'
        verde = (0, 100, 0)
        font = py.font.Font(fonte, 50)
        medium_font = py.font.Font(fonte, 25)
        small_font = py.font.Font(fonte, 20)
        self.screen.blit(imagem, (141, 161), (131, 131, 419, 319))

        game_over = font.render("Game Over", True, (0, 100, 0))
        pontuacao = medium_font.render("Pontos: " + str(self.points.pontos_final), True, verde)
        reiniciar = small_font.render('Reiniciar (R)', True, verde)
        quitar = small_font.render('Sair (Q)', True, verde)

        self.screen.blit(game_over, (160, 175))
        self.screen.blit(pontuacao, (245, 300))
        self.screen.blit(reiniciar, (165, 435))
        self.screen.blit(quitar, (380, 435))
