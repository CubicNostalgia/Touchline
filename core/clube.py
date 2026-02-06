class Clube:
    def __init__(self, id: str, nome: str, forca: int, reputacao: int = 1):
        self.id = id
        self.nome = nome
        self.forca = forca 
        self.reputacao = reputacao

    def __repr__(self):
        return self.nome
