import pygame


class timer:
    def __init__(self):
        self.image = pygame.image.load('./entities/itens_imagens/clock.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.tempo = 10
        self.font = pygame.font.Font("./fontes/PixelDigivolve.otf", 30)
        self.ultimo_tick = pygame.time.get_ticks()

    def contar_tempo(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_tick >= 1000:  # Atualiza a cada 1 segundo
            self.tempo -= 1
            self.ultimo_tick = agora

    def resetar(self):
        self.tempo = 60

    def desenhar(self, screen):
        timer_tela = self.font.render(str(self.tempo), True, (255, 255, 255))
        screen.blit(self.image, (545, 25))
        screen.blit(timer_tela, (580, 20))

