import pygame
import sys
from tela_jogo import Tela


class Carro(pygame.sprite.Sprite):  # Herda de Sprite
    def __init__(self, img, x, y):
        super().__init__()  # Inicializa o Sprite
        
        # Carregar imagem e redimensionar
        img= pygame.image.load(r'C:\Users\User\Downloads\vrum.png')
        escala = 120 / img.get_rect().height
        largura = int(img.get_rect().width * escala)
        altura = int(img.get_rect().height * escala)
        self.image = pygame.transform.scale(img, (largura, altura))
        
        # Configuração do retângulo para posicionamento
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
        self.hitbox = self.rect.inflate(-40, -20)
        
    def mover(self, direcao, limite_esq, limite_dir):
        if direcao == "direita" and self.rect.center[0] < limite_dir:
            self.rect.x += 100
        elif direcao == "esquerda" and self.rect.center[0] > limite_esq:
            self.rect.x -= 100
        
        self.hitbox.centery = self.rect.centery
        self.hitbox.centerx = self.rect.centerx
        
         
