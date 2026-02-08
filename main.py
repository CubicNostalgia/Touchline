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

    liga = Liga("Campeonato Brasileiro — Série A", clubes)
    temporada = Temporada(liga)

    while True:
        print("\n📋 Menu")
        print("[1] Exibir elenco")
        print("[2] Simular próxima rodada")
        print("[3] Simular temporada inteira")
        print("[0] Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            exibir_elenco(clube_usuario)

        elif opcao == "2":
            temporada.simular_proxima_rodada()

        elif opcao == "3":
            temporada.jogar_temporada_completa()
            break

        elif opcao == "0":
            print("\nSaindo do jogo...")
            break


if __name__ == "__main__":
    main()
