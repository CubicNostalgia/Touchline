class Jogador:
    def __init__(self, nome: str, over: int, posicao: str):
        self.nome = nome
        self.over = over
        self.posicao = posicao

    def __repr__(self):
        return f"{self.nome} ({self.posicao}) — {self.over}"
