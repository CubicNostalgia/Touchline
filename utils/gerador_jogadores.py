import random
from core.jogador import Jogador

# -----------------------------
# Bases de nomes (genéricos)
# -----------------------------

PRENOMES = [
    "Gabriel", "Lucas", "Matheus", "Vitor", "Bruno", "Felipe",
    "Igor", "Caio", "Rafael", "Diego", "Renan", "Arthur",
    "Pedro", "Thiago", "André", "Leandro", "Victor", "Henrique",
    "Danilo", "Eduardo", "Samuel", "João", "Marcos", "Alex",
    "Murilo", "Vinicius", "Allan", "Guilherme", "Rodrigo",
    "Nicolas", "Pablo", "Luan", "Wesley", "Yuri", "Patrick",
    "Matheusinho", "Paulinho", "Brayan", "Alan", "Gustavo", "Sandro", "Estêvão",
    "Isac"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira",
    "Lima", "Ferreira", "da Costa", "Rodrigues", "Almeida",
    "Ribeiro", "Carvalho", "Gomes", "Martins", "Araujo",
    "Rocha", "Barbosa", "Teixeira", "Correia", "Farias",
    "Macedo", "Nogueira", "Batista", "Freitas", "Pacheco",
    "Moura", "Cavalcante", "Rezende", "Tavares", "Monteiro",
    "Peixoto", "Bandeira", "Fonseca", "Lopes", "Amaral",
    "Guedes", "Moreira", "Assis", "Vasconcelos", "Rangel", "Menezes",
    "Melo", "Gonçalves"
]

APELIDOS = [
    "Juninho", "Paulinho", "Marcinho", "Dudu", "Nenem",
    "Biel", "Careca", "Zezinho", "Pedrinho", "Ronaldinho",
    "Vitinho", "Luquinhas", "Thiaguinho", "Fernandinho", "Tetê",
    "Fumaça"
]

# -----------------------------
# Geração de dados
# -----------------------------

def gerar_nome():
    # 20% de chance de apelido
    if random.random() < 0.2:
        return random.choice(APELIDOS)

    return f"{random.choice(PRENOMES)} {random.choice(SOBRENOMES)}"


def gerar_over(forca_base: int):
    """
    Gera over próximo da média do clube.
    Evita outliers irreais.
    """
    variacao = random.choice([-2, -1, 0, 0, 0, 1, 2])
    over = forca_base + variacao
    return max(60, min(82, over))


def gerar_elenco(forca_base: int):
    elenco = []

    composicao = {
        "GOL": 3,
        "DEF": 7,
        "MEI": 6,
        "ATA": 6
    }

    for posicao, quantidade in composicao.items():
        for _ in range(quantidade):
            nome = gerar_nome()
            over = gerar_over(forca_base)
            elenco.append(Jogador(nome, over, posicao))

    return elenco
