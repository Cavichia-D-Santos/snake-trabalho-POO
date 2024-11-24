import pygame as py
from entities.snake import Snake
from entities.food import Food
from entities.colisao import colisoes
from entities.points import points
from telas.cenarioMain import tela
from entities.enemy_shooter import enemy_shooter
from entities.timer import timer

py.init()  # Inicializador do jogo
clock = py.time.Clock()

# Variáveis de jogo
gameRunning = True  # Para testar telas
v_jogo = 10
alturaTela = 640
larguraTela = 640

# Instancias
snake = Snake()
food = Food()
points = points()
tela = tela(alturaTela, larguraTela, points)
timer = timer()

enemy_shooter_bottom = enemy_shooter(190, 570, 2000, 90, 20)
enemy_shooter_up = enemy_shooter(370, -10, 2000, 270, 20)
enemy_shooter_left = enemy_shooter(-10, 190, 2000, 0, 20)
enemy_shooter_right = enemy_shooter(570, 370, 2000, 180, 20)

colisao = colisoes(snake, food, points, larguraTela, alturaTela, enemy_shooter_bottom.bullets,
                   enemy_shooter_up.bullets, enemy_shooter_left.bullets, enemy_shooter_right.bullets)

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
                    timer.resetar()
                    colisao.status = 'vivo'
                    gameRunning = True
                elif event.key == py.K_q:
                    py.quit()
                    exit()

        # funções
        snake.movimento()
        pontos = points.pontos_final
        # desenhar na tela (obs.: ordem de cima para baixo)
        fase = 1
        if colisao.status != 'morto':
            if fase == 1:
                tela.tela_jogo()
                food.desenhar(tela.screen)
                snake.cobra_tela(tela.screen)
                points.desenhar(tela.screen)
                timer.desenhar(tela.screen)
                timer.contar_tempo()

                enemy_shooter_bottom.desenhar(tela.screen)
                enemy_shooter_up.desenhar(tela.screen)
                enemy_shooter_left.desenhar(tela.screen)
                enemy_shooter_right.desenhar(tela.screen)

                enemy_shooter_bottom.atirar()
                enemy_shooter_up.atirar()
                enemy_shooter_left.atirar()
                enemy_shooter_right.atirar()

                enemy_shooter_bottom.atualizar_tiros(tela.screen)
                enemy_shooter_up.atualizar_tiros(tela.screen)
                enemy_shooter_left.atualizar_tiros(tela.screen)
                enemy_shooter_right.atualizar_tiros(tela.screen)

                if timer.tempo == -1:
                    colisao.status = 'morto'

                if points.pontos == 10:
                    fase = 2

            if fase == 2:
                print('sou foda')
        else:
            points.total_pontos()
            tela.tela_fim_jogo()

        colisao.snake_food()
        colisao.snake_snake()
        colisao.snake_paredes()
        colisao.snake_tiro1()
        colisao.snake_tiro2()
        colisao.snake_tiro3()
        colisao.snake_tiro4()

        # jogo (refresh da tela e tick)
        py.display.update()
        clock.tick(v_jogo)
