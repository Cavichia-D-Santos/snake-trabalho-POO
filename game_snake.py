import pygame as py
from entities.snake import Snake
from entities.food import Food
from telas.cenarioMain import tela

py.init()  # Inicializador do jogo
clock = py.time.Clock() ## This method has to do with FPS

# Instancias
snake = Snake([(120, 120), (90, 120), (80, 120)])   # Pos. inicial pra cobra; Coloquei aqui pra tentar
                                                    # arrumar alguns conflitos, mas por enquanto nao consegui
food = Food()
tela = tela(640, 640)

# Variaveis de jogo
consumido = True
gameRunning = True # Para testar telas
pos = snake.corpo

while True: ## Loop para encerrar o jogo, caso o usuário precione o botão de fechar pagina, e para que todo o jogo aconteça.
    consumido = False

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

    cabeca_x, cabeca_y = snake.corpo[0]

    if cabeca_x == food.x and cabeca_y == food.y:
        print("Colisão!")
        snake.aumentar_tamanho()
        consumido = True

        #food.consumida()

    if gameRunning: #Teste de troca entre telas
        tela.tela_jogo()
    else:
        tela.tela_fim_jogo()

    snake.movimento()
    snake.cobra_tela(tela.screen)
    food.food_tela(tela.screen, consumido) #Inclui 'consumido' pra gerar uma nova posicao sempre que a comida encosta no player
    py.display.update()
    clock.tick(10)