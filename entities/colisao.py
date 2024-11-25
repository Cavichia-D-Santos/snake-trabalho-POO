from entities import enemy_shooter

class colisoes:
    def __init__(self, snake, food, points, largura_tela, altura_tela, bullet_bottom,
                 bullet_up, bullet_left, bullet_right, azul, azul_bt):
        self.food = food
        self.snake = snake
        self.points = points
        self.cabeca_x = None
        self.cabeca_y = None
        self.larg = largura_tela
        self.alt = altura_tela
        self.status = 'vivo'
        self.bullet1 = bullet_bottom
        self.bullet2 = bullet_up
        self.bullet3 = bullet_left
        self.bullet4 = bullet_right
        self.azul = azul
        self.azul_bt = azul_bt

    # colisões separadas por entidade (cobra com comida; cobra com paredes; cobra com corpo)
    def snake_food(self):
        self.cabeca_x, self.cabeca_y = self.snake.corpo[0]  # pos. x e y da cabeca
        if self.cabeca_x == self.food.x and self.cabeca_y == self.food.y:
            self.snake.aumentar_tamanho()
            self.food.food_coord()
            self.points.pontuacao()

    def snake_paredes(self):
        if self.cabeca_x < 0 or self.cabeca_x > self.larg - 20 or self.cabeca_y < 0 or self.cabeca_y > self.alt - 20:
            self.status = 'morto'

    def snake_snake(self):
        # Obs: Usei 'slicing' no for para manipular o array do corpo: lista[início:fim:passo]
        for corpo_x, corpo_y in self.snake.corpo[2:]:  # Verifica cada tupla do corpo, ignorando a cabeca (índice 0)
            if corpo_x == self.cabeca_x and corpo_y == self.cabeca_y:
                self.status = 'morto'

#INIMIGO DA FASE 1
    def snake_tiro1(self):
        for bala in self.bullet1[:]:
            if self.cabeca_x == bala.rect.x and self.cabeca_y == bala.rect.y:
                self.status = 'morto'

    def snake_tiro2(self):
        for bala in self.bullet2[:]:
            if self.cabeca_x == bala.rect.x and self.cabeca_y == bala.rect.y:
                self.status = 'morto'

    def snake_tiro3(self):
        for bala in self.bullet3[:]:
            if self.cabeca_x == bala.rect.x and self.cabeca_y == bala.rect.y:
                self.status = 'morto'

    def snake_tiro4(self):
        for bala in self.bullet4[:]:
            if self.cabeca_x == bala.rect.x and self.cabeca_y == bala.rect.y:
                self.status = 'morto'

# INIMIGO DA FASE 2
    def snake_pathEnemy(self, pathEnemy):
        x, y = pathEnemy.inimigo_Head # pos. canto esquerdo do inimigo
        self.cabeca_x, self.cabeca_y = self.snake.corpo[0]
        # print(f"Cabeça da cobra: {self.cabeca_x}, {self.cabeca_y}")
        # print(f"Inimigo: ({x}, {y}) até ({x + pathEnemy.hitbox}, {y + pathEnemy.hitbox})")
        if x <= self.cabeca_x < x + pathEnemy.hitbox and y <= self.cabeca_y < y + pathEnemy.hitbox:
            self.status = 'morto'

# INIMIGO DA FASE 3
    def snake_azul(self):
        for item in self.azul[:]:
            if self.cabeca_x == item.x and self.cabeca_y == item.y:
                self.status = 'morto'

    def snake_boss_azul(self):
        if self.snake.cabeca_rect.colliderect(self.azul_bt.rect):
            self.status = 'morto'
