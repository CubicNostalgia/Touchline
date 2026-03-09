def mensagem_boas_vindas_objetivos(clube):
    print(f"\n🏢 A diretoria lhe dá as boas-vindas ao {clube.nome}!")
    print("Seus objetivos pros primeiros meses de trabalho são:")
    for objetivo in gerar_objetivos_por_clube(clube):
        print(f"- {objetivo}")


def gerar_objetivos_por_clube(clube):
    objetivos = []

    if clube.forca >= 76 or clube.reputacao >= 4:
        objetivos.append("Alcançar a semifinal do estadual")
        objetivos.append("Alcançar a 3ª fase da Copa do Brasil")
    elif clube.forca >= 72:
        objetivos.append("Chegar às quartas de final do estadual")
        objetivos.append("Alcançar a 2ª fase da Copa do Brasil")
    else:
        objetivos.append("Fazer campanha estável no estadual")
        objetivos.append("Passar da 1ª fase da Copa do Brasil")

    objetivos.append("Utilizar pelo menos 3 jogadores da Academia de Base")
    return objetivos


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
