import pygame 

class Objeto_base(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        super().__init__()
        
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        
        self.hitbox = self.rect.inflate(-40,-40)
        
    def mover(self,velocidade):
        self.rect.y += velocidade
        self.hitbox.y = self.rect.y 
        self.hitbox.centery = self.rect.centery
        self.hitbox.centerx = self.rect.centerx

class Objeto1(Objeto_base):
    def __init__(self,x,y):
        super().__init__(r'./Downloads/cone.png',x,y)
                
class Objeto2(Objeto_base):
    def __init__(self,x,y):
        super().__init__(r'./Downloads/buraco.png',x,y)
        
        
