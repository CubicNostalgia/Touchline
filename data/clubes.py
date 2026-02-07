from core.clube import Clube
from utils.gerador_jogadores import gerar_elenco


def carregar_clubes_serie_a():
    dados = [
        {"id": "flamen", "nome": "FLAMEN", "forca_base": 80, "reputacao": 5},
        {"id": "palmei", "nome": "PALMEI", "forca_base": 79, "reputacao": 5},
        {"id": "corinthns", "nome": "CORINTHNS", "forca_base": 77, "reputacao": 5},
        {"id": "s_paulo", "nome": "S PAULO", "forca_base": 77, "reputacao": 5},
        {"id": "gremio", "nome": "GREMIO", "forca_base": 76, "reputacao": 4},
        {"id": "inter", "nome": "INTER", "forca_base": 76, "reputacao": 4},
        {"id": "atl_mineiro", "nome": "ATL MINEIRO", "forca_base": 77, "reputacao": 4},
        {"id": "ath_paranaense", "nome": "ATH PARANAENSE", "forca_base": 74, "reputacao": 3},
        {"id": "bahia", "nome": "BAHIA", "forca_base": 75, "reputacao": 3},
        {"id": "braga", "nome": "BRAGA", "forca_base": 74, "reputacao": 3},
        {"id": "fluminse", "nome": "FLUMINSE", "forca_base": 74, "reputacao": 3},
        {"id": "vasco", "nome": "VASCO", "forca_base": 73, "reputacao": 3},
        {"id": "vitoria", "nome": "VITORIA", "forca_base": 73, "reputacao": 3},
        {"id": "santos", "nome": "SANTOS", "forca_base": 74, "reputacao": 4},
        {"id": "crtiba", "nome": "CRTIBA", "forca_base": 71, "reputacao": 3},
        {"id": "chape", "nome": "CHAPE", "forca_base": 71, "reputacao": 2},
        {"id": "remo", "nome": "REMO", "forca_base": 70, "reputacao": 2},
        {"id": "mirassol", "nome": "MIRASSOL", "forca_base": 71, "reputacao": 2},
        {"id": "botafo", "nome": "BOTAFO", "forca_base": 76, "reputacao": 4},
        {"id": "cruzro", "nome": "CRUZRO", "forca_base": 75, "reputacao": 4},
    ]

    clubes = []
    for c in dados:
        elenco = gerar_elenco(c["forca_base"])
        clubes.append(
            Clube(
                id=c["id"],
                nome=c["nome"],
                elenco=elenco,
                reputacao=c["reputacao"]
            )
        )

    return clubes
