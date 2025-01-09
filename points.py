import pygame

class Point:
    def __init__(self, fonte=30, cor=(255,255,255)):
        self.score = 0 
        self.fonte = pygame.font.Font(None, fonte)
        self.cor = cor
        
    def atualização_pontuacao(self,valor=1):
        self.score += valor
        
    def exibir_score(self, tela):
        texto = f'Score:{int(self.score)}'
        superficie_texto = self.fonte.render(texto, True, self.cor)
        tela.blit(superficie_texto,(10,10))
