import pygame
import sys
class Inicializacao:
    def __init__(self, tela):
        self.tela = tela  # A tela principal será usada aqui

    def mostrar_mensagem(self, mensagem, cor=(255, 255, 255)):
        font = pygame.font.Font(None, 36)
        texto = font.render(mensagem, True, cor)
        texto_rect = texto.get_rect(center=(self.tela.largura // 2, self.tela.altura // 2))
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

            self.tela.cor_tela()  # Preenche a tela com a cor de fundo
            self.mostrar_mensagem("Pressione ENTER para iniciar")
            self.tela.atualizar()