import pygame as py

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
        fundoCor = (0, 0, 0)
        self.screen.fill(fundoCor)