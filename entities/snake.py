import pygame as py


class Snake:
    def __init__(self):
        self.corpo = ([(100, 100), (90, 100), (80, 100)])
        self.direcao = 'RIGHT'
        self.nova_cabeca = None
        self.cor_corpo = (0, 0, 0)
        self.grid = 20  # Tamanho de cada bloco na tela
        self.cabeca_rect = None

    def movimento(self):  # Seta os movimentos da cobrinha
        cabeca_x, cabeca_y = self.corpo[0]  # x e y aqui representam a coordenada da cabeça
        self.nova_cabeca = (self.corpo[0])  # variável que armarzena o input do evento

        if self.direcao == 'RIGHT':
            self.nova_cabeca = (cabeca_x + self.grid, cabeca_y)
        elif self.direcao == 'LEFT':
            self.nova_cabeca = (cabeca_x - self.grid, cabeca_y)
        elif self.direcao == 'UP':
            self.nova_cabeca = (cabeca_x, cabeca_y - self.grid)
        elif self.direcao == 'DOWN':
            self.nova_cabeca = (cabeca_x, cabeca_y + self.grid)

        self.corpo = [self.nova_cabeca] + self.corpo[
                                          :-1]  # Adiciona a nova posição captada pelo evento e apaga a última tupla

        # COLOQUEI A LINHA ABAIXO PARA COLIDIR COM O INIMIGO 3!!! -MALISSE
        self.cabeca_rect = py.Rect(cabeca_x, cabeca_y, 20, 20)

    def cobra_tela(self, screen):
        for i, cor in enumerate(self.corpo): # Alterna cores entre segmentos; Calcula pelo numero da pos. do segmento
            if i %2 == 0:
                self.cor_corpo = (0, 180, 0)
            else:
                self.cor_corpo = (0, 80, 0)

            py.draw.rect(screen, self.cor_corpo, py.Rect(cor[0], cor[1], self.grid, self.grid))

    def aumentar_tamanho(self):
        self.corpo = [self.nova_cabeca] + self.corpo

    def resetar(self):
        self.corpo = ([(100, 100), (90, 100), (80, 100)])
        self.direcao = 'RIGHT'
