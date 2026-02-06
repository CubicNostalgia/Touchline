from core.liga import Liga
from core.temporada import Temporada

from data.clubes import carregar_clubes_serie_a


def main():
    print("\n⚽ TOUCHLINE — Football Manager (Alpha)\n")

    clubes_serie_a = carregar_clubes_serie_a()

    serie_a = Liga(
        nome="Campeonato Brasileiro — Série A",
        clubes=clubes_serie_a
    )

    temporada = Temporada(serie_a)

    temporada.jogar()


if __name__ == "__main__":
    main()
