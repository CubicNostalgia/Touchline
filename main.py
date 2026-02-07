from data.clubes import carregar_clubes_serie_a
from core.liga import Liga
from core.temporada import Temporada
from ui.exibir_elenco import exibir_elenco


def escolher_clube(clubes):
    print("\nEscolha seu clube:\n")

    for i, clube in enumerate(clubes, start=1):
        print(f"{i}. {clube.nome}")

    while True:
        escolha = input("\nNúmero do clube: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(clubes):
                return clubes[escolha - 1]


def main():
    print("⚽ TOUCHLINE — Football Manager (Alpha)\n")

    clubes = carregar_clubes_serie_a()
    clube_usuario = escolher_clube(clubes)

    exibir_elenco(clube_usuario)

    input("\nPressione ENTER para iniciar a temporada...")

    liga = Liga("Campeonato Brasileiro — Série A", clubes)
    temporada = Temporada(liga)
    temporada.jogar()


if __name__ == "__main__":
    main()
