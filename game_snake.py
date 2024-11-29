import time

import pygame as py
from entities.snake import Snake
from entities.food import Food
from entities.colisao import colisoes
from entities.points import points
from entities.enemies.pathEnemy import PathEnemy
from telas.cenarioMain import tela
from entities.enemies.enemy_shooter import enemy_shooter
from entities.timer import timer
from entities.enemies.enemy_blue_team import Blue_team
from entities.enemies.enemy_firewall import firewall

py.init()  # Inicializador do jogo
clock = py.time.Clock()

# Variáveis de jogo
gameRunning = True  # Para testar telas
v_jogo = 10
alturaTela = 640
larguraTela = 640
fase = 0
passarFase = 1

# Instancias
snake = Snake()
food = Food()
points = points()
bt_enemy = Blue_team(food)
firew = firewall()
tela = tela(alturaTela, larguraTela, points)
timer = timer()

path1_init = [(580,60)]
path2_init = [(60,580)]
pathEn1 = PathEnemy(path1_init)
pathEn2 = PathEnemy(path2_init)
# pathEn3 = PathEnemy()

enemy_shooter_bottom = enemy_shooter(190, 570, 2000, 90, 20)
enemy_shooter_up = enemy_shooter(370, -10, 2000, 270, 20)
enemy_shooter_left = enemy_shooter(-10, 190, 2000, 0, 20)
enemy_shooter_right = enemy_shooter(570, 370, 2000, 180, 20)

colisao = colisoes(snake, food, points, larguraTela, alturaTela, enemy_shooter_bottom.bullets,
                   enemy_shooter_up.bullets, enemy_shooter_left.bullets, enemy_shooter_right.bullets,
                   bt_enemy.azuis, bt_enemy, firew)

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
                elif event.key == py.K_w:
                    if passarFase == 1 or passarFase == 2 or passarFase == 3:
                        fase += 1
                        passarFase = 0
                elif event.key == py.K_q:
                    py.quit()
                    exit()

        pontos = points.pontos_final

        if passarFase == 1:  # alternar entre tela menu
                tela.tela_menu()

        # desenhar na tela (obs.: ordem de cima para baixo)
        if colisao.status != 'morto':

            if fase == 1:
                snake.movimento()
                tela.tela_jogo()
                food.desenhar(tela.screen)
                snake.cobra_tela(tela.screen)
                points.desenhar(tela.screen)
                timer.desenhar(tela.screen)
                timer.contar_tempo()
                points.objetivo = 10

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

                colisao.snake_tiro1()
                colisao.snake_tiro2()
                colisao.snake_tiro3()
                colisao.snake_tiro4()

                if timer.tempo == -1:
                    colisao.status = 'morto'

                if points.pontos == 10:
                    snake.resetar()
                    timer.resetar()
                    passarFase = 2
                    tela.telas_intermediarias(fase)

            if fase == 2:
                snake.movimento()
                colisao.snake_pathEnemy(pathEn1)
                colisao.snake_pathEnemy(pathEn2)
                colisao.snake_firewall(firew)
                colisao.food_wall(firew)

                pos1 = pathEn1.posicoes = [(580, 60), (580, 580), (60, 580), (60, 60)]
                pathEn1.andar(pos1, snake)
                pos2 = pathEn2.posicoes = [(60, 580), (60, 60), (580, 60), (580, 580)]
                pathEn2.andar(pos2, snake)

                tela.tela_jogo()
                snake.cobra_tela(tela.screen)
                firew.desenhar(tela.screen)
                food.desenhar(tela.screen)
                points.desenhar(tela.screen)
                pathEn1.desenhar(tela.screen)
                pathEn2.desenhar(tela.screen)
                timer.desenhar(tela.screen)
                timer.contar_tempo()
                points.objetivo = 20

                if timer.tempo == -1:
                    colisao.status = 'morto'

                if points.pontos == 20:
                    snake.resetar()
                    timer.resetar()
                    passarFase = 3
                    tela.telas_intermediarias(fase)

            if fase == 3:
                snake.movimento()
                tela.tela_jogo()
                food.desenhar(tela.screen)
                snake.cobra_tela(tela.screen)
                points.desenhar(tela.screen)
                bt_enemy.destruir_chao()
                bt_enemy.desenhar_chao(tela.screen)
                bt_enemy.desenhar_inimigo(tela.screen)
                bt_enemy.mover(larguraTela, alturaTela)
                timer.desenhar(tela.screen)
                timer.contar_tempo()
                points.objetivo = 30

                colisao.snake_azul()
                colisao.snake_boss_azul()

                if timer.tempo == -1:
                    colisao.status = 'morto'

                if points.pontos == 30:
                    tela.tela_parabens()
                    py.display.update()
                    gameRunning = False
                    py.time.delay(5000)
                    exit()

        else:
            fase = 1
            timer.resetar()
            points.total_pontos()
            tela.tela_fim_jogo()

        colisao.snake_food()
        colisao.snake_snake()
        colisao.snake_paredes()

        # jogo (refresh da tela e tick)
        py.display.update()
        clock.tick(v_jogo)
