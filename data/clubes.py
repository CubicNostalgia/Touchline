from core.clube import Clube

def carregar_clubes_serie_a():
    dados = [
    {
        "id": "flamen",
        "nome": "FLAMEN",
        "forca": 80,
        "reputacao": 5
    },
    {
        "id": "palmei",
        "nome": "PALMEI",
        "forca": 79,
        "reputacao": 5
    },
    {
        "id": "corinthns",
        "nome": "CORINTHNS",
        "forca": 77,
        "reputacao": 4
    },
    {
        "id": "s_paulo",
        "nome": "S PAULO",
        "forca": 77,
        "reputacao": 4
    },
    {
        "id": "gremio",
        "nome": "GREMIO",
        "forca": 76,
        "reputacao": 4
    },
    {
        "id": "inter",
        "nome": "INTER",
        "forca": 76,
        "reputacao": 4
    },
    {
        "id": "atl_mineiro",
        "nome": "ATL MINEIRO",
        "forca": 77,
        "reputacao": 4
    },
    {
        "id": "ath_paranaense",
        "nome": "ATH PARANAENSE",
        "forca": 74,
        "reputacao": 4
    },
    {
        "id": "bahia",
        "nome": "BAHIA",
        "forca": 75,
        "reputacao": 3
    },
    {
        "id": "braga",
        "nome": "BRAGA",
        "forca": 74,
        "reputacao": 3
    },
    {
        "id": "fluminse",
        "nome": "FLUMINSE",
        "forca": 74,
        "reputacao": 3
    },
    {
        "id": "vasco",
        "nome": "VASCO",
        "forca": 73,
        "reputacao": 3
    },
    {
        "id": "vitoria",
        "nome": "VITORIA",
        "forca": 73,
        "reputacao": 3
    },
    {
        "id": "santos",
        "nome": "SANTOS",
        "forca": 73,
        "reputacao": 4
    },
    {
        "id": "crtiba",
        "nome": "CRTIBA",
        "forca": 71,
        "reputacao": 3
    },
    {
        "id": "chape",
        "nome": "CHAPE",
        "forca": 71,
        "reputacao": 2
    },
    {
        "id": "remo",
        "nome": "REMO",
        "forca": 70,
        "reputacao": 2
    },
    {
        "id": "mirassol",
        "nome": "MIRASSOL",
        "forca": 71,
        "reputacao": 2
    },
    {
        "id": "botafo",
        "nome": "BOTAFO",
        "forca": 76,
        "reputacao": 4
    },
    {
        "id": "cruzro",
        "nome": "CRUZRO",
        "forca": 75,
        "reputacao": 4
    }
]
    
    return [Clube(**c) for c in dados]
