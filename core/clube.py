class Clube:
    def __init__(self, id: str, nome: str, elenco: list, reputacao: int):
        self.id = id
        self.nome = nome
        self.elenco = elenco
        self.reputacao = reputacao

    @property
    def forca(self):
        return round(sum(j.over for j in self.elenco) / len(self.elenco))

    # -----------------------------
    # Estatísticas do elenco
    # -----------------------------

    def media_por_posicao(self):
        medias = {}
        for posicao in ["GOL", "DEF", "MEI", "ATA"]:
            jogadores = [j for j in self.elenco if j.posicao == posicao]
            if jogadores:
                medias[posicao] = round(
                    sum(j.over for j in jogadores) / len(jogadores)
                )
        return medias

    def melhor_jogador(self):
        return max(self.elenco, key=lambda j: j.over)

    def pior_jogador(self):
        return min(self.elenco, key=lambda j: j.over)
