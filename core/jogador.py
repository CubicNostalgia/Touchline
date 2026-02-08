class Jogador:
    def __init__(self, nome: str, overall: int, posicao: str):
        self.nome = nome
        self.overall = overall
        self.posicao = posicao

    def __repr__(self):
        return f"{self.nome} ({self.posicao}) — {self.overall}"
