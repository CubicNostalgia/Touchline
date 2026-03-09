from datetime import datetime, date, timedelta
from data.database import DATAS_FIFA_2026, PAUSAS_TORNEIOS_2026


def _gerar_rodadas(clubes):
    calendario = []
    clubes = clubes[:]
    if len(clubes) % 2 != 0:
        clubes.append(None)

    n = len(clubes)
    for _ in range(n - 1):
        rodada = []
        for i in range(n // 2):
            casa, fora = clubes[i], clubes[n - 1 - i]
            if casa and fora:
                rodada.append((casa, fora))
        calendario.append(rodada)
        clubes = [clubes[0]] + [clubes[-1]] + clubes[1:-1]
    return calendario


def _data_bloqueada(dia: date):
    for inicio, fim in DATAS_FIFA_2026:
        if inicio <= dia <= fim:
            return True
    for pausa in PAUSAS_TORNEIOS_2026:
        if pausa["inicio"] <= dia <= pausa["fim"]:
            return True
    return False


def _proxima_data_valida(cursor, dia_semana):
    while True:
        if cursor.weekday() == dia_semana and not _data_bloqueada(cursor.date()):
            return cursor
        cursor += timedelta(days=1)


def gerar_calendario_dinamico(clubes, inicio=datetime(2026, 1, 12, 20, 0)):
    ida = _gerar_rodadas(clubes)
    volta = [[(fora, casa) for casa, fora in rodada] for rodada in ida]
    jogos = ida + volta

    calendario = []
    cursor = inicio
    slots = [(0, (20, 0), "Campeonato Brasileiro — Série A"), (3, (19, 30), "Campeonato Brasileiro — Série A")]

    for idx, rodada in enumerate(jogos, start=1):
        dia_semana, horario, comp_nome = slots[(idx - 1) % len(slots)]
        cursor = _proxima_data_valida(cursor, dia_semana)
        data_jogo = datetime(cursor.year, cursor.month, cursor.day, horario[0], horario[1])

        calendario.append(
            {
                "rodada": idx,
                "competicao": comp_nome,
                "data": data_jogo,
                "partidas": rodada,
            }
        )
        cursor += timedelta(days=2)

    return calendario
