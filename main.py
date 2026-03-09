from data.clubes import carregar_clubes_serie_a
from core.liga import Liga
from core.temporada import Temporada
from ui.exibir_elenco import exibir_elenco
from ui.mensagens import mensagem_boas_vindas_objetivos
from data.database import HIERARQUIA_COMPETICOES


def escolher_clube(clubes):
    print("\nEscolha seu clube:\n")
    for i, clube in enumerate(clubes, start=1):
        print(f"{i}. {clube.nome}")

    while True:
        escolha = input("\nNúmero do clube: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(clubes):
            return clubes[int(escolha) - 1]


def personalizar_escalacao(clube):
    print("\n⚙️ Personalização de escalação")
    print("[1] 4-3-3")
    print("[2] 4-4-2")
    print("[3] 3-5-2")
    op = input("Formação: ").strip()
    mapa = {"1": "4-3-3", "2": "4-4-2", "3": "3-5-2"}
    clube.definir_formacao(mapa.get(op, "4-3-3"))

    custom = input("Deseja escolher manualmente os titulares? (s/n): ").lower().strip()
    if custom != "s":
        return

    for idx, j in enumerate(clube.elenco):
        print(f"[{idx}] {j.nome} - {j.posicao} OVR {j.overall}")
    ids = input("Digite 11 índices separados por vírgula: ").split(",")
    try:
        clube.definir_titulares([int(x.strip()) for x in ids])
    except ValueError:
        print("Entrada inválida. Escalação automática mantida.")


def main():
    print("⚽ TOUCHLINE — Football Manager (Alpha)\n")
    print("Hierarquia de competições:", " < ".join(HIERARQUIA_COMPETICOES))

    clubes = carregar_clubes_serie_a()
    clube_usuario = escolher_clube(clubes)

    mensagem_boas_vindas_objetivos(clube_usuario)
    personalizar_escalacao(clube_usuario)

    liga = Liga("Campeonato Brasileiro — Série A", clubes)
    temporada = Temporada(liga)

    while True:
        print("\n📋 Menu")
        print("[1] Exibir elenco")
        print("[2] Simular próxima rodada")
        print("[3] Simular temporada inteira")
        print("[4] Ajustar formação/titulares")
        print("[0] Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            exibir_elenco(clube_usuario)
        elif opcao == "2":
            temporada.simular_proxima_rodada()
        elif opcao == "3":
            temporada.jogar_temporada_completa()
            break
        elif opcao == "4":
            personalizar_escalacao(clube_usuario)
        elif opcao == "0":
            print("\nSaindo do jogo...")
            break


if __name__ == "__main__":
    main()
