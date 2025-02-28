import pygame
import random
from outros_obj import Objeto1, Objeto2
from points import Point
from gerenciador_pontuacoes import GerenciadorPontuacoes


class Jogo:
    def __init__(self, tela):
        self.tela = tela
        self.gerenciador_pontuacoes = GerenciadorPontuacoes()
        self.running = True
        self.carro = None
        self.pontilhado_a = 0
        self.sprites = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.posicao_obstaculo = None
        self.tempo_obstaculo = 0
        self.pontuacao = Point()
        
        self.limite_esq = 200
        self.limite_dir = 400
        
        self.min_distancia = 150

    def pista(self, speed):
        # Dimensões da pista
        pista_x = 150
        pista_y = 0
        largura_pista = 300
        altura_pista = self.tela.altura

        road = (pista_x, pista_y, largura_pista, altura_pista)
        marca_esq = (150, 0, pista_x - 140, self.tela.altura)
        marca_dir = (450, 0, pista_x - 140, self.tela.altura)

        linha_esq = 250
        linha_dir = 350
        tamanho_pont = 20
        espaco_pont = 40

        # Animação dos pontilhados se movendo
        self.pontilhado_a += speed
        if self.pontilhado_a >= tamanho_pont + espaco_pont:
            self.pontilhado_a = 0

        pygame.draw.rect(self.tela.screen, (128, 128, 128), road)
        pygame.draw.rect(self.tela.screen, (255, 255, 225), marca_esq)
        pygame.draw.rect(self.tela.screen, (225, 255, 225), marca_dir)

        for i in range(0, self.tela.altura, tamanho_pont + espaco_pont):
            y_pos = i + self.pontilhado_a
            pygame.draw.rect(self.tela.screen, (225, 225, 0), (linha_esq, y_pos, 4, tamanho_pont))
            pygame.draw.rect(self.tela.screen, (225, 225, 0), (linha_dir + 2, y_pos, 4, tamanho_pont))
            

    def criar_obstaculo(self):
        if pygame.time.get_ticks() - self.tempo_obstaculo > 2000: 
            posicoes_pos = [200, 300, 400]  # Posições válidas na pista
            espacamento_minimo = 150
            
            for obstaculo in self.obstaculos:
                if obstaculo.rect.top < espacamento_minimo:  
                    return  
                
            if self.posicao_obstaculo in posicoes_pos:
                posicoes_pos.remove(self.posicao_obstaculo)
        
            x_pos = random.choice(posicoes_pos)
            self.posicao_obstaculo = x_pos  
            
       
            if random.choice([True, False]):
                obstaculo = Objeto1(x_pos, -50)
            else:
                obstaculo = Objeto2(x_pos, -50)
        
        # Adicionar o obstáculo aos grupos
            self.obstaculos.add(obstaculo)
            self.sprites.add(obstaculo)
            self.tempo_obstaculo = pygame.time.get_ticks()  

    def verificar_colisao(self):
        for obstaculo in self.obstaculos:
           if self.carro.hitbox.colliderect(obstaculo.hitbox):
            print("Você perdeu.")
            self.running = False
            return True
        return False
            

    def executar(self, clock, fps, carro):
        self.carro = carro
        self.sprites.add(self.carro)
        self.mostrando_scores = False

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.mostrando_scores = True
                    elif event.key == pygame.K_RETURN and self.mostrando_scores:
                        self.mostrando_scores = False
                    elif event.key == pygame.K_RIGHT:
                        self.carro.mover("direita", 200, 400)
                    elif event.key == pygame.K_LEFT:
                        self.carro.mover("esquerda", 200, 400)

            clock.tick(fps)
            self.tela.cor_tela()
            
            if self.mostrando_scores:
                self.mostrar_scores()
            else:
                self.tela.cor_tela()
                self.pista(2)
                self.criar_obstaculo()
                self.pontuacao.atualização_pontuacao()

                for obstaculo in self.obstaculos:
                    obstaculo.mover(2)

                # Remove obstáculos que saem da tela
                    if obstaculo.rect.top > self.tela.altura:
                        obstaculo.kill()
                
                if self.verificar_colisao():
                    break
                
                self.sprites.draw(self.tela.screen)
                self.pontuacao.exibir_score(self.tela.screen)
            self.tela.atualizar() 
