def gerar_calendario(clubes):
    """
    Gera um calendário simples de turno único (ida).
    O returno será tratado fora.
    """
    calendario = []

    clubes = clubes[:]
    if len(clubes) % 2 != 0:
        clubes.append(None)  # bye

    n = len(clubes)
    rodadas = n - 1
    metade = n // 2

    for _ in range(rodadas):
        rodada = []

        for i in range(metade):
            casa = clubes[i]
            fora = clubes[n - 1 - i]

            if casa is not None and fora is not None:
                rodada.append((casa, fora))

        calendario.append(rodada)

        # Rotação (Round-robin clássico)
        clubes = [clubes[0]] + [clubes[-1]] + clubes[1:-1]

    return calendario
