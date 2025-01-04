import pygame
import sys

from tela_jogo import Tela
from inicializacao_jogo import Inicializacao
from jogo_jogo import Jogo
from carro_jogo import Carro
                                
# Configuração da tela
tela = Tela(600, 600, (100, 255, 100))  

# Exibindo a inicialização
inicializacao = Inicializacao(tela)
inicializacao.aguardar_acao(tela)  # Aguarda o jogador pressionar ENTER para começar

carro = Carro(r'C:\Users\User\Downloads\vrum.png', 300, 500)

# Inicia o jogo
jogo = Jogo(tela)
jogo.executar(pygame.time.Clock(), 120, carro)

pygame.quit()
sys.exit()
