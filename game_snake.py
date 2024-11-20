import pygame as py
from entities.snake import Snake
from entities.food import Food
from entities.colisao import colisoes
from entities.points import points
from telas.cenarioMain import tela

py.init()  # Inicializador do jogo
clock = py.time.Clock() ## This method has to do with FPS

# Variaveis de jogo
gameRunning = True # Para testar telas
velocJogo = 10
alturaTela = 640
larguraTela = 640

# Instancias
tela = tela (alturaTela, larguraTela)
snake = Snake()
food = Food()
points = points()
colisao = colisoes(snake, food, points, larguraTela, alturaTela)

while True: ## Loop para encerrar o jogo, caso o usuário precione o botão de fechar pagina, e para que todo o jogo aconteça.
    while gameRunning: # Para reiniciar o jogo se o player perder
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()

            elif event.type == py.KEYDOWN: ## Capta o evento da tecla precionada (metodo KEYDOWN);
                                           ## É proibido que o usuario tente pressionar uma direção oposta a direção atual para evitar
                                           ## que a cobra volte e colida consigo mesma.
                if event.key == py.K_LEFT and snake.direcao != 'RIGHT':
                    snake.direcao = 'LEFT'
                elif event.key == py.K_RIGHT and snake.direcao != 'LEFT':
                    snake.direcao = 'RIGHT'
                elif event.key == py.K_UP and snake.direcao != 'DOWN':
                    snake.direcao = 'UP'
                elif event.key == py.K_DOWN and snake.direcao != 'UP':
                    snake.direcao = 'DOWN'

        # funcoes
        snake.movimento()

        # desenhar na tela (obs: ordem de cima para baixo)
        tela.tela_jogo()
        food.desenhar(tela.screen)
        snake.cobra_tela(tela.screen)
        points.desenhar(tela.screen)

        # colisoes
        colisao.snake_food()
        colisao.snake_paredes()
        colisao.snake_snake()

        # jogo (refresh da tela e tick)
        py.display.update()
        clock.tick(velocJogo)