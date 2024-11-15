import pygame as py


class Snake():
    def __init__(self, largura_tela, altura_tela):
        self.corpo = [(100, 100), (90, 100), (80, 100)] ## A cobrinha está dividida em três segmentos - A medida que o jogo avança,
                                                        ## o número de segmentos aumenta;
                                                        ## Cada segmento é representado por coordenadas x e y;
                                                        ## A cabeça da cobra está na posição [0].
        self.direcao = 'RIGHT'
        self.cor_corpo = (0, 255, 0)
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

    def movimento(self): ## Seta os movimentos da cobrinha
        cabeca_x, cabeca_y = self.corpo[0] ## x e y aqui representam a coordenada da cabeça (lá ele).

        nova_cabeca = (cabeca_x, cabeca_y) ## variável que armarzana o input do evento.

        if self.direcao == 'RIGHT':
            nova_cabeca = (cabeca_x + 10, cabeca_y)
        elif self.direcao == 'LEFT':
            nova_cabeca = (cabeca_x - 10, cabeca_y)
        elif self.direcao == 'UP':
            nova_cabeca = (cabeca_x, cabeca_y - 10)
        elif self.direcao == 'DOWN':
            nova_cabeca = (cabeca_x, cabeca_y + 10)

        self.corpo = [nova_cabeca] + self.corpo[:-1] ## Adiciona a nova posição captada pelo evento e apaga a última tupla

    def cobra_tela(self, screen): ##Desenha a cobrinha na tela!
        for pos in self.corpo:
            py.draw.rect(screen, self.cor_corpo, py.Rect(pos[0], pos[1], 15, 15))

    #def aumentar_tamanho(self):
