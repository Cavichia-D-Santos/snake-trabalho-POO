import pygame
import random
from entities.enemy_bt_attack import Blue_floor


class Blue_team:
    def __init__(self, food):
        self.image = pygame.image.load('./entities/inimigos_Sprites/blue_team.png')
        self.image = pygame.transform.scale(self.image, (250, 210))
        self.rect = self.image.get_rect(topleft=(194, 240))
        self.ultimo_ataque = pygame.time.get_ticks()
        self.azuis = []
        self.food = food
        self.velocidade = 12
        self.direcao_x = 1  # 1 = direita -1 = esquerda

    def desenhar_inimigo(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def mover(self, largura_tela, altura_tela):
        self.rect.x += self.velocidade * self.direcao_x
        if self.rect.right >= largura_tela or self.rect.left <= 0:
            self.direcao_x *= -1

    def destruir_chao(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_ataque >= 1000:
            x = random.randint(0, 31) * 20
            y = random.randint(0, 31) * 20
            novo_ataque = Blue_floor(x, y)
            if x != self.food.x and y != self.food.y:
                self.azuis.append(novo_ataque)
                self.ultimo_ataque = agora

    def desenhar_chao(self, screen):
        for item in self.azuis:
            x = item.x
            y = item.y
            pygame.draw.rect(screen, (0, 0, 255), (x, y, 20, 20))
