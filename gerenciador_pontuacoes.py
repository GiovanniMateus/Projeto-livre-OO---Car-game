import json


class GerenciadorPontuacoes:
    def __init__(self, arquivo='pontuacoes.json'):
        self.arquivo = arquivo
        self.pontuacoes = self.carregar_pontuacoes()
    

    def carregar_pontuacoes(self):
        try:
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_pontuacao(self, nome, pontuacao):
        nova_pontuacao = ({'nome': nome, 'pontuacao': pontuacao})
        self.pontuacoes.append(nova_pontuacao)
        self.pontuacoes = sorted(self.pontuacoes, key=lambda x: x['pontuacao'], reverse=True)[:10]

        with open(self.arquivo, 'w') as f:
            json.dump(self.pontuacoes, f)
