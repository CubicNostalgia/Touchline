def exibir_elenco(clube):
    print(f"\n📋 Elenco do {clube.nome} ({clube.formacao})")
    print("-" * 64)

    for posicao in ["GOL", "DEF", "MEI", "ATA"]:
        print(f"\n{posicao}")
        print("-" * 64)
        for jogador in clube.elenco:
            if jogador.posicao == posicao:
                print(
                    f"{jogador.nome.ljust(22)} OVR:{str(jogador.overall).ljust(3)} "
                    f"POT:{str(jogador.potencial).ljust(3)} ID:{str(jogador.idade).ljust(2)} "
                    f"FAD:{int(jogador.fadiga):>2}"
                )

    print("\n📊 Médias")
    print("-" * 20)
    print(f"Média geral: {clube.forca}")

    medias = clube.media_por_posicao()
    for pos, media in medias.items():
        print(f"{pos}: {media}")

    melhor = clube.melhor_jogador()
    pior = clube.pior_jogador()

    print("\n⭐ Destaques")
    print("-" * 20)
    print(f"Melhor jogador: {melhor.nome} ({melhor.overall})")
    print(f"Pior jogador:   {pior.nome} ({pior.overall})")
