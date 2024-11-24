import pygame

class Bullet:
    def __init__(self, velocidade,  x_rect, y_rect, angulo):
        self.rect = pygame.Rect(x_rect, y_rect, 20, 20)  # Hitbox do tiro
        self.cor = (255, 255, 255)
        self.velocidade = velocidade
        self.x_rect = x_rect
        self.y_rect = y_rect
        self.angulo = angulo

    def desenhar_tiro(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)  # Desenha o tiro na tela

    def movimentar_tiro(self):
        if self.angulo == 90:
            self.rect.y -= self.velocidade
        if self.angulo == 270:
            self.rect.y += self.velocidade
        if self.angulo == 0:
            self.rect.x += self.velocidade
        if self.angulo == 180:
            self.rect.x -= self.velocidade

