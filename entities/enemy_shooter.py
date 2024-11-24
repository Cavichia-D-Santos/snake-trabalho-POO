import pygame

from entities.bullet import Bullet


class enemy_shooter:
    def __init__(self, x, y, tempo_ataque, angulo, vel_tiro):
        self.image = pygame.image.load('./entities/inimigos_imagens/shooter.png')
        self.image = pygame.transform.scale(self.image, (80, 80))  # Ajusta o tamanho da imagem
        self.rect = self.image.get_rect(topleft=(x, y))
        self.tempo_ataque = tempo_ataque
        self.bullets = []
        self.ultimo_ataque = pygame.time.get_ticks()
        self.angulo = angulo
        self.vel_tiro = vel_tiro

    def atirar(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_ataque >= self.tempo_ataque:
            # cria tiro
            x_bala = self.rect.centerx - 10
            y_bala = self.rect.centery - 10
            nova_bala = Bullet(self.vel_tiro, x_bala, y_bala, self.angulo)
            self.bullets.append(nova_bala)
            self.ultimo_ataque = agora

    def desenhar(self, tela):
        imagem_rotacionada = pygame.transform.rotate(self.image, self.angulo)
        self.rect = imagem_rotacionada.get_rect(center=self.rect.center)
        tela.blit(imagem_rotacionada, self.rect.topleft)

    def atualizar_tiros(self, tela):
        # Atualiza e desenha todas as balas
        for bala in self.bullets[:]:  # Copia da lista para evitar problemas ao remover
            bala.movimentar_tiro()
            bala.desenhar_tiro(tela)
            # Remove a bala se ela sair da tela
            if bala.rect.right < 0 or bala.rect.left > tela.get_width() or bala.rect.top > tela.get_height() or bala.rect.bottom < 0:
                self.bullets.remove(bala)


# class Tiro:
#     def __init__(self, x, y, velocidade, atirador):
#         self.rect = pygame.Rect(x, y, 20, 20)  # Hitbox do tiro
#         self.cor = (255, 255, 255)
#         self.velocidade = velocidade
#         self.atirador = atirador
#
#
#
#     def movimentar(self):
#
#         if self.atirador =
#
