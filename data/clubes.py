from core.clube import Clube
from utils.gerador_jogadores import gerar_elenco
from data.database import CLUBES_SERIE_A, CLUBES_SERIE_B_2026, SELECOES


def _instanciar_clubes(base):
    clubes = []
    for c in base:
        clubes.append(
            Clube(
                id=c["id"],
                nome=c["nome"],
                elenco=gerar_elenco(c["forca_base"]),
                reputacao=c.get("reputacao", 1),
            )
        )
    return clubes


def carregar_clubes_serie_a():
    return _instanciar_clubes(CLUBES_SERIE_A)


def carregar_clubes_serie_b_2026():
    base = [{"id": nome.lower().replace(" ", "_"), "nome": nome, "forca_base": 70, "reputacao": 2} for nome in CLUBES_SERIE_B_2026]
    return _instanciar_clubes(base)


def carregar_selecoes():
    base = [{"id": s["id"], "nome": s["nome"], "forca_base": s["forca_base"], "reputacao": 5} for s in SELECOES]
    return _instanciar_clubes(base)
