def exibir_elenco(clube):
    print(f"\n📋 Elenco do {clube.nome}")
    print("-" * 40)

    for posicao in ["GOL", "DEF", "MEI", "ATA"]:
        print(f"\n{posicao}")
        print("-" * 20)
        for jogador in clube.elenco:
            if jogador.posicao == posicao:
                print(f"{jogador.nome.ljust(18)} {jogador.over}")

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
    print(f"Melhor jogador: {melhor.nome} ({melhor.over})")
    print(f"Pior jogador:   {pior.nome} ({pior.over})")
