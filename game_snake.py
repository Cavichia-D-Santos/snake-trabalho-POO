import pygame as py

py.init() ## Inicializador do jogo


screen = py.display.set_mode((800,400)) ## Tamanho da tela e nome da página
py.display.set_caption("O melhor jogo da cobrinha do Brasil")

clock = py.time.Clock() ## This method has to do with FPS 


background_collor = (137, 207, 240)
screen.fill(background_collor)

py.display.update()

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
            py.draw.rect(screen, self.cor_corpo, py.Rect(pos[0], pos[1], 15, 15)) ## py.draw.rect é usada para desenhar um retangulos 
                                                                                  ## na tela a cada segmento da cobra; 
                                                                                  ## py.rect define a posição do retangulo e tamanho
## Rectangles are used to place a surface much more efficiently and THEY HELP WITH DETECTING COLLISIONS. When you use rectangles, you
## separete placing images in two different steps: Surface for image information and placement via rectangle

snake = Snake(800, 400) ## Criação de um instancia para o jogador. Aqui é setado o lugar que a cobrinha aparece no mapa

while True: ## Loop para encerrar o jogo, caso o usuário precione o botão de fechar pagina, e para que todo o jogo aconteça.
    for event in py.event.get():
        if event.type == py.QUIT: 
            py.quit()
            exit() 

        elif event.type == py.KEYDOWN: ## Capta o evento da tecla precionada (metodo KEYDOWN);
                                       ## É proibido que o usuario tente precionar uma direção oposta a direção atual para evitar 
                                       ## que a cobra volte e colida consigo mesma.
            if event.key == py.K_LEFT and snake.direcao != 'RIGHT': 
                snake.direcao = 'LEFT'
            elif event.key == py.K_RIGHT and snake.direcao != 'LEFT':  
                snake.direcao = 'RIGHT'
            elif event.key == py.K_UP and snake.direcao != 'DOWN':
                snake.direcao = 'UP'
            elif event.key == py.K_DOWN and snake.direcao != 'UP':
                snake.direcao = 'DOWN'

    snake.movimento()
    screen.fill(background_collor)
    snake.cobra_tela(screen)
    py.display.update()
    clock.tick(10)

