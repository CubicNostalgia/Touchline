def mensagem_fim_temporada(posicao, pontos, total_clubes):
    print("\n📌 RESULTADO DA TEMPORADA\n")

    if posicao <= 4:
        print(f"🎉 Sensacional! Você terminou em {posicao}º, garantindo vaga direta na Libertadores!")
    elif posicao == 5:
        print(f"💪 Faltou pouco! {posicao}º dá vaga na fase preliminar da Libertadores.")
    elif posicao <= total_clubes // 2:
        print(f"🙂 {posicao}º é uma colocação segura, mas sem vaga continental.")
    else:
        print(f"😬 {posicao}º... cuidado com a zona de rebaixamento!")

    print(f"📊 Pontos: {pontos}")
