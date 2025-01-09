import json
import pygame
import sys

class Inicializacao:
    def __init__(self, tela):
        self.tela = tela  # A tela principal será usada aqui

    def mostrar_mensagem(self, mensagem, y=150, cor=(255, 255, 255)):
        font = pygame.font.Font(None, 36)
        texto = font.render(mensagem, True, cor)
        texto_rect = texto.get_rect(center=(self.tela.largura // 2, y))
        self.tela.screen.blit(texto, texto_rect)

    def aguardar_acao(self,tela):
        aguardando = True
        while aguardando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        tela.att_cor ((0,255,0))
                        aguardando = False  
                    elif event.key == pygame.K_s:
                        self.mostrar_scores()

            self.tela.cor_tela()  # Preenche a tela com a cor de fundo
            self.mostrar_mensagem("Pressione ENTER para iniciar ou s para ver os scores")
            self.tela.atualizar()
            
    def mostrar_scores(self):
        try:
            with open("pontuacoes.json", "r") as f:
                dados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = []  # Se o arquivo não existir ou estiver vazio

        font = pygame.font.Font(None, 36)
        y = 50
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Voltar para a tela inicial ao pressionar ENTER
                        return
                    
            self.tela.cor_tela()
            self.mostrar_mensagem("Pontuações:", y=20)
            for score in dados:
                texto = f"{score['nome']}: {score['pontuacao']}"
                superficie_texto = font.render(texto, True, (255, 255, 255))
                self.tela.screen.blit(superficie_texto, (50, y))
                y += 40
            self.tela.atualizar()
            pygame.time.wait(2000)
            
    def entrada_nome(self):
        nome = ''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(nome)>0:
                        return nome
                    elif event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    elif len(nome) < 10 and event.unicode.isalnum():
                        nome += event.unicode
                        
            self.tela.cor_tela()
            self.mostrar_mensagem (f"Seu Nome: {nome}", y=100, cor=(255, 255, 255))
            self.mostrar_mensagem("Pressione ENTER para confirmar", y=200, cor=(255, 255, 255))
            self.tela.atualizar()
