from datetime import date

HIERARQUIA_COMPETICOES = [
    "estadual",
    "regional",
    "nacional",
    "internacional",
    "intercontinental",
    "mundial",
]

COMPETICOES = {
    "bra_a": {
        "id": "bra_a",
        "nome": "Campeonato Brasileiro — Série A",
        "nivel": "nacional",
    },
    "bra_b": {
        "id": "bra_b",
        "nome": "Campeonato Brasileiro — Série B",
        "nivel": "nacional",
    },
    "paulistao": {
        "id": "paulistao",
        "nome": "Campeonato Paulista",
        "nivel": "estadual",
    },
    "carioca": {
        "id": "carioca",
        "nome": "Campeonato Carioca",
        "nivel": "estadual",
    },
    "pre_lib": {
        "id": "pre_lib",
        "nome": "Pré-Libertadores",
        "nivel": "internacional",
    },
}

DATAS_FIFA_2026 = [
    (date(2026, 3, 23), date(2026, 3, 31)),
    (date(2026, 6, 1), date(2026, 6, 9)),
    (date(2026, 9, 7), date(2026, 9, 15)),
    (date(2026, 10, 5), date(2026, 10, 13)),
    (date(2026, 11, 9), date(2026, 11, 17)),
]

PAUSAS_TORNEIOS_2026 = [
    {
        "nome": "Copa do Mundo",
        "inicio": date(2026, 6, 11),
        "fim": date(2026, 7, 19),
    }
]

CLUBES_SERIE_A = [
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

CLUBES_SERIE_B_2026 = [
    "AMERIC MG", "ATHL CLUB", "ATL GOIANIEN", "AVAI", "BOTAFO SP", "CRB", "CEARA", "CRICIUM",
    "CUIABA", "FORTAL", "GOIAS", "JUVNTUD RS", "LONDRIN", "NOVORIZON", "NAUTCO", "OPERAR PR",
    "PNT PRETA", "SPORT", "S BERNAR", "VIL NOVA GO",
]

SELECOES = [
    {"id": "brasil", "nome": "BRASIL", "forca_base": 84},
    {"id": "argentina", "nome": "ARGENTINA", "forca_base": 85},
    {"id": "franca", "nome": "FRANCA", "forca_base": 86},
    {"id": "inglaterra", "nome": "INGLATERRA", "forca_base": 84},
]
