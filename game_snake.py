import pygame as py
from entities import snake
from entities import food

py.init()  # Inicializador do jogo


screen = py.display.set_mode((640, 640))  # Tamanho da tela e nome da página
py.display.set_caption("Snake.exe")

clock = py.time.Clock() ## This method has to do with FPS 


background_color = (208, 202, 146)
screen.fill(background_color)

py.display.update()                                                                                 ## na tela a cada segmento da cobra;
                                                                                  ## py.rect define a posição do retangulo e tamanho
## Rectangles are used to place a surface much more efficiently and THEY HELP WITH DETECTING COLLISIONS. When you use rectangles, you
## separete placing images in two different steps: Surface for image information and placement via rectangle

snake = snake.Snake(800, 400) ## Criação de um instancia para o jogador. Aqui é setado o lugar que a cobrinha aparece no mapa

while True: ## Loop para encerrar o jogo, caso o usuário precione o botão de fechar pagina, e para que todo o jogo aconteça.
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

    snake.movimento()
    screen.fill(background_color)
    snake.cobra_tela(screen)
    food.Food.food_screen(screen) #Ainda não entendi o erro. verificar!!!
    py.display.update()
    clock.tick(10)

