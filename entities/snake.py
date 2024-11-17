import pygame as py
grid = 20 # Tamanho de cada bloco na tela

class Snake():
    def __init__(self):
        self.corpo = [(120, 120), (90, 120), (80, 120)] ## A cobrinha está dividida em três segmentos - A medida que o jogo avança,
                                                        ## o número de segmentos aumenta;
                                                        ## Cada segmento é representado por coordenadas x e y;
                                                        ## A cabeça da cobra está na posição [0].
        self.direcao = 'RIGHT'
        self.cor_corpo = (0, 180, 0)

    def movimento(self): ## Seta os movimentos da cobrinha
        cabeca_x, cabeca_y = self.corpo[0] ## x e y aqui representam a coordenada da cabeça (lá ele).

        nova_cabeca = (cabeca_x, cabeca_y) ## variável que armarzana o input do evento.

        if self.direcao == 'RIGHT':
            nova_cabeca = (cabeca_x + grid, cabeca_y)
        elif self.direcao == 'LEFT':
            nova_cabeca = (cabeca_x - grid, cabeca_y)
        elif self.direcao == 'UP':
            nova_cabeca = (cabeca_x, cabeca_y - grid)
        elif self.direcao == 'DOWN':
            nova_cabeca = (cabeca_x, cabeca_y + grid)

        self.corpo = [nova_cabeca] + self.corpo[:-1] ## Adiciona a nova posição captada pelo evento e apaga a última tupla

    def cobra_tela(self, screen): ##Desenha a cobrinha na tela!
        for pos in self.corpo:
            py.draw.rect(screen, self.cor_corpo, py.Rect(pos[0], pos[1], grid, grid))

    #def aumentar_tamanho(self):

    #def gameOver(self):