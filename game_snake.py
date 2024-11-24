import pygame as py
from entities.snake import Snake
from entities.food import Food
from entities.colisao import colisoes
from entities.points import points
from entities.pathEnemy import PathEnemy
from telas.cenarioMain import tela

py.init()  # Inicializador do jogo
clock = py.time.Clock()

# Variáveis de jogo
gameRunning = True  # Para testar telas
v_jogo = 10
alturaTela = 640
larguraTela = 640
fase = 1

# Instancias
snake = Snake()
food = Food()
points = points()
pathEnemy = PathEnemy()
tela = tela(alturaTela, larguraTela, points)
colisao = colisoes(snake, food, points, larguraTela, alturaTela)

#Inimigos

while True:  # Loop para encerrar o jogo, caso o usuário pressione o botão de fechar pagina, e para que todo o jogo aconteça.
    while gameRunning:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()

            elif event.type == py.KEYDOWN:
                if event.key == py.K_LEFT and snake.direcao != 'RIGHT':
                    snake.direcao = 'LEFT'
                elif event.key == py.K_RIGHT and snake.direcao != 'LEFT':
                    snake.direcao = 'RIGHT'
                elif event.key == py.K_UP and snake.direcao != 'DOWN':
                    snake.direcao = 'UP'
                elif event.key == py.K_DOWN and snake.direcao != 'UP':
                    snake.direcao = 'DOWN'
                elif event.key == py.K_r:
                    points.resetar()
                    snake.resetar()
                    colisao.status = 'vivo'
                    gameRunning = True
                elif event.key == py.K_q:
                    py.quit()
                    exit()

        if points.pontos == 3:
            fase = 2

        # funções
        snake.movimento()
        pontos = points.pontos_final
        # desenhar na tela (obs.: ordem de cima para baixo)
        if colisao.status != 'morto':
            tela.tela_jogo()
            food.desenhar(tela.screen)
            snake.cobra_tela(tela.screen)
            points.desenhar(tela.screen)
            pathEnemy.desenhar(tela.screen)

            if fase == 1:
                # TESTANDO INIMIGO
                aaa = pathEnemy.posicoes = [(100, 400), (400, 400)]
                pathEnemy.andar(aaa, snake)

            elif fase == 2:
                aaa = pathEnemy.posicoes = [(400, 200), (400, 400)]
                pathEnemy.andar(aaa, snake)

        else:
            points.total_pontos()
            tela.tela_fim_jogo()
            fase = 1

        colisao.snake_food()
        colisao.snake_snake()
        colisao.snake_paredes()
        colisao.snake_pathEnemy(pathEnemy)

        # jogo (refresh da tela e tick)
        py.display.update()
        clock.tick(v_jogo)