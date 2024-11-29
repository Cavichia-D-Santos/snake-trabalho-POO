import pygame as py
import pygame.image

class tela:  # Características da tela e da grid
    def __init__(self, altura_tela, largura_tela, points):
        self.larguraTela = largura_tela
        self.alturaTela = altura_tela
        self.screen = py.display.set_mode((self.alturaTela, self.larguraTela))
        self.points = points  # Referência ao objeto points
        self.preto = (0, 0, 0)
        py.display.set_caption("Snake.exe")  # Nome da página

    def tela_menu(self):
        cor_texto = (255, 255, 255)
        fonte = './fontes/PixelDigivolve.otf'
        font = py.font.Font(fonte, 50)
        medium_font = py.font.Font(fonte, 25)
        imagem = py.image.load('./entities/imagens_src/fundo.png').convert()
        imagemFundo = py.transform.scale(imagem, (640, 640))

        titulo = font.render("WORM ATTACK", True, cor_texto)
        subtitulo = medium_font.render("Invadir. Capturar. Vencer.", True, cor_texto)
        startBtn = medium_font.render('Começar jogo (W)', True, cor_texto)

        self.screen.fill(self.preto)
        self.screen.blit(imagemFundo, (0, 0))
        self.screen.blit(titulo, (140, 80))
        self.screen.blit(subtitulo, (140, 150))
        self.screen.blit(startBtn, (200, 400))


    def tela_jogo(self):
        linhas_fundo = (0, 100, 0)
        tamanho_grid = 20
        self.screen.fill(self.preto)

        for x in range(tamanho_grid, self.larguraTela, tamanho_grid):
            py.draw.line(self.screen, linhas_fundo, (x, 0), (x, self.alturaTela))
        for y in range(tamanho_grid, self.alturaTela, tamanho_grid):
            py.draw.line(self.screen, linhas_fundo, (0, y), (self.larguraTela, y))

    def tela_fim_jogo(self):
        imagem = pygame.image.load('./telas/tela-game-over.png')
        fonte = './fontes/Gameplay.ttf'
        verde = (0, 100, 0)
        font = py.font.Font(fonte, 50)
        medium_font = py.font.Font(fonte, 25)
        small_font = py.font.Font(fonte, 20)
        self.screen.blit(imagem, (141, 161), (131, 131, 419, 319))

        game_over = font.render("Game Over", True, (0, 100, 0))
        pontuacao = medium_font.render("Pontos: " + str(self.points.pontos_final), True, verde)
        reiniciar = small_font.render('Reiniciar (R)', True, verde)
        quitar = small_font.render('Sair (Q)', True, verde)

        self.screen.blit(game_over, (160, 175))
        self.screen.blit(pontuacao, (245, 300))
        self.screen.blit(reiniciar, (165, 435))
        self.screen.blit(quitar, (380, 435))

    def tela_parabens(self):
        imagem = pygame.image.load('./telas/tela-game-over.png')
        fonte = './fontes/Gameplay.ttf'
        texto = (255, 255, 255)
        font = py.font.Font(fonte, 50)
        medium_font = py.font.Font(fonte, 20)
        small_font = py.font.Font(fonte, 18)
        self.screen.blit(imagem, (141, 161), (131, 131, 419, 319))

        parabens = font.render("VITORIA!", True, (0, 100, 0))
        mensagem1 = small_font.render("O Blue Team foi vencido", True, texto)
        mensagem2 = small_font.render("e o worm dominou toda a rede!", True, texto)

        self.screen.blit(parabens, (205, 175))
        self.screen.blit(mensagem1, (185, 300))
        self.screen.blit(mensagem2, (150, 330))

    #Telas entre niveis
    def telas_intermediarias(self, fase):
        faseTela = fase
        cor_texto = (255, 255, 255)
        textoGrande = f"Fase {fase} concluída!"
        fonte = './fontes/PixelDigivolve.otf'
        font = py.font.Font(fonte, 50)
        small_font = py.font.Font(fonte, 20)
        self.tela_jogo()

        if faseTela == 1:
            info = [
                "   Evite abrir links ou anexos suspeitos, seja",
                "           na internet ou por e-mail. Reporte",
                "   comportamentos incomuns, a equipe de TI está",
                "   disponível para ajudá-lo em caso de dúvidas."
            ]
            texto = []

            textoMain = font.render(textoGrande, True, cor_texto)
            for linha in info:
                linha_renderizada = small_font.render(linha, True, cor_texto)
                texto.append(linha_renderizada)
            textoBtn = small_font.render('Continuar (W)', True, cor_texto)

            self.screen.blit(textoMain, (80, 80))
            for i, linha in enumerate(texto):
                self.screen.blit(linha, (25, 218 + i * small_font.get_linesize()))
            self.screen.blit(textoBtn, (240, 450))

        if faseTela == 2:
            info = [
                "   Seus dispositivos precisam ser protegidos!",
                "   Tenha um firewall e um antivirus de qualidade",
                "para assegurar a segurança dos seus dados. Usar",
                "ambos é fundamental como crimes ciberneticos."
            ]
            texto = []

            textoMain = font.render(textoGrande, True, cor_texto)
            for linha in info:
                linha_renderizada = small_font.render(linha, True, cor_texto)
                texto.append(linha_renderizada)
            textoBtn = small_font.render('Continuar (W)', True, cor_texto)

            self.screen.blit(textoMain, (80, 80))
            for i, linha in enumerate(texto):
                self.screen.blit(linha, (25, 218 + i * small_font.get_linesize()))
            self.screen.blit(textoBtn, (240, 450))