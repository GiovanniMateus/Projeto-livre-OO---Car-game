import pygame
import sys

from tela_jogo import Tela
from inicializacao_jogo import Inicializacao
from jogo_jogo import Jogo
from carro_jogo import Carro
from gerenciador_pontuacoes import GerenciadorPontuacoes
from points import Point
                                
# Configuração da tela
tela = Tela(700, 600, (100, 255, 100))  

# Exibindo a inicialização
inicializacao = Inicializacao(tela)
inicializacao.aguardar_acao(tela)  # Aguarda o jogador pressionar ENTER para começar

nome_jogador = inicializacao.entrada_nome()

gerenciador = GerenciadorPontuacoes()

pontuacao = Point()

carro = Carro(r'./Downloads/vrum.png', 300, 500)


# Inicia o jogo
jogo = Jogo(tela)
jogo.executar(pygame.time.Clock(), 120, carro)

jogo.pontuacao.atualização_pontuacao()

gerenciador.salvar_pontuacao(nome_jogador, jogo.pontuacao.score)

pygame.quit()
sys.exit()

