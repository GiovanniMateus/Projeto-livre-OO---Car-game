import pygame
pygame.init()
class Tela:
    def __init__(self, largura, altura, cor):
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Meu Jogo")

    def cor_tela(self):
        if self.screen:
            self.screen.fill(self.cor)
    
    def att_cor(self,nova_cor):
        self.cor = nova_cor

    def atualizar(self):
        if self.screen:
            pygame.display.flip()