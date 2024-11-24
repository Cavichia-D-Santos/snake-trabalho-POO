class colisoes:
    def __init__(self, snake, food, points, largura_tela, altura_tela):
        self.food = food
        self.snake = snake
        self.points = points
        self.cabeca_x = None
        self.cabeca_y = None
        self.larg = largura_tela
        self.alt = altura_tela
        self.status = 'vivo'

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

    def snake_pathEnemy(self, pathEnemy):
        x, y = pathEnemy.inimigo_Head # pos. canto esquerdo do inimigo
        self.cabeca_x, self.cabeca_y = self.snake.corpo[0]
        # print(f"Cabeça da cobra: {self.cabeca_x}, {self.cabeca_y}")
        # print(f"Inimigo: ({x}, {y}) até ({x + pathEnemy.hitbox}, {y + pathEnemy.hitbox})")
        if x <= self.cabeca_x < x + pathEnemy.hitbox and y <= self.cabeca_y < y + pathEnemy.hitbox:
            self.status = 'morto'