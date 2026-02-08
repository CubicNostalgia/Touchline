class Clube:

    def __init__(self, id, nome, elenco, reputacao=1):
        self.id = id
        self.nome = nome
        self.elenco = elenco
        self.reputacao = reputacao

    @property
    def forca(self):
        titulares = self.elenco[:11]
        return round(
            sum(j.overall for j in titulares) / len(titulares),
            1
        )


    def forca_titular(self):
        titulares = []

        titulares += sorted(
            [j for j in self.elenco if j.posicao == "GOL"],
            key=lambda j: j.overall,
            reverse=True
        )[:1]

        titulares += sorted(
            [j for j in self.elenco if j.posicao == "DEF"],
            key=lambda j: j.overall,
            reverse=True
        )[:4]

        titulares += sorted(
            [j for j in self.elenco if j.posicao == "MEI"],
            key=lambda j: j.overall,
            reverse=True
        )[:3]

        titulares += sorted(
            [j for j in self.elenco if j.posicao == "ATA"],
            key=lambda j: j.overall,
            reverse=True
        )[:3]

        return round(
            sum(j.overall for j in titulares) / len(titulares),
            1
        )
    
    # ... (métodos __init__, forca e forca_titular que já existem) ...

    def media_por_posicao(self):
        medias = {}
        for pos in ["GOL", "DEF", "MEI", "ATA"]:
            # Filtra os jogadores daquela posição
            jogadores = [j for j in self.elenco if j.posicao == pos]
            
            if jogadores:
                media = sum(j.overall for j in jogadores) / len(jogadores)
                medias[pos] = round(media, 1)
            else:
                medias[pos] = 0
        return medias

    def melhor_jogador(self):
        # Retorna o jogador com maior overall
        return max(self.elenco, key=lambda j: j.overall)

    def pior_jogador(self):
        # Retorna o jogador com menor overall
        return min(self.elenco, key=lambda j: j.overall)
    

