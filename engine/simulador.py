import random


def simular_partida(casa, fora):
    """
    Simula uma partida baseada na força dos clubes.
    Retorna (gols_casa, gols_fora)
    """

    vantagem_mando = 5

    forca_casa = casa.forca + vantagem_mando
    forca_fora = fora.forca

    diferenca = forca_casa - forca_fora

    # Base de gols
    gols_casa = random.randint(0, 2)
    gols_fora = random.randint(0, 2)

    # Ajuste pela diferença de força
    ajuste = round(diferenca / 20)

    gols_casa = max(0, gols_casa + ajuste)
    gols_fora = max(0, gols_fora - ajuste)

    return gols_casa, gols_fora
