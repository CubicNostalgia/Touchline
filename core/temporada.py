from engine.calendario import gerar_calendario_dinamico
from engine.simulador import simular_partida


class Temporada:
    def __init__(self, liga):
        self.liga = liga
        self.calendario_completo = gerar_calendario_dinamico(liga.clubes)
        self.rodada_atual = 0
        self.tabela = {
            clube: {"pontos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "gols_pro": 0, "gols_contra": 0}
            for clube in liga.clubes
        }

    def simular_proxima_rodada(self):
        if self.rodada_atual >= len(self.calendario_completo):
            print("\n🏁 A temporada já terminou.\n")
            return False

        rodada_info = self.calendario_completo[self.rodada_atual]
        data_txt = rodada_info["data"].strftime("%d/%m/%Y %H:%M")
        print(f"\n🕒 Rodada {rodada_info['rodada']} — {rodada_info['competicao']} — {data_txt}")

        if self.rodada_atual > 0:
            dias = (rodada_info["data"].date() - self.calendario_completo[self.rodada_atual - 1]["data"].date()).days
            for clube in self.liga.clubes:
                clube.recuperar_elenco(max(1, dias))

        self._jogar_rodada(rodada_info["partidas"])
        self.rodada_atual += 1

        if self.rodada_atual == len(self.calendario_completo):
            print("🏁 Fim da temporada\n")
            self.exibir_tabela_final()
        return True

    def jogar_temporada_completa(self):
        print(f"\n🏁 Início da temporada — {self.liga.nome}\n")
        while self.simular_proxima_rodada():
            pass

    def _jogar_rodada(self, rodada):
        for casa, fora in rodada:
            gols_casa, gols_fora = simular_partida(casa, fora)
            self._registrar_partida(casa, fora, gols_casa, gols_fora)
            casa.aplicar_partida()
            fora.aplicar_partida()
            print(f"  {casa.nome:>12} {gols_casa} x {gols_fora} {fora.nome:<12}")
        print()

    def _registrar_partida(self, casa, fora, gols_casa, gols_fora):
        t_casa = self.tabela[casa]
        t_fora = self.tabela[fora]
        t_casa["gols_pro"] += gols_casa
        t_casa["gols_contra"] += gols_fora
        t_fora["gols_pro"] += gols_fora
        t_fora["gols_contra"] += gols_casa

        if gols_casa > gols_fora:
            t_casa["vitorias"] += 1
            t_casa["pontos"] += 3
            t_fora["derrotas"] += 1
            casa.atualizar_desenvolvimento("V")
            fora.atualizar_desenvolvimento("D")
        elif gols_casa < gols_fora:
            t_fora["vitorias"] += 1
            t_fora["pontos"] += 3
            t_casa["derrotas"] += 1
            fora.atualizar_desenvolvimento("V")
            casa.atualizar_desenvolvimento("D")
        else:
            t_casa["empates"] += 1
            t_fora["empates"] += 1
            t_casa["pontos"] += 1
            t_fora["pontos"] += 1
            casa.atualizar_desenvolvimento("E")
            fora.atualizar_desenvolvimento("E")

    def classificacao(self):
        return sorted(
            self.tabela.items(),
            key=lambda item: (item[1]["pontos"], item[1]["gols_pro"] - item[1]["gols_contra"], item[1]["gols_pro"]),
            reverse=True,
        )

    def exibir_tabela_final(self):
        classificacao_final = self.classificacao()
        print(f"\n🏆 CLASSIFICAÇÃO FINAL — {self.liga.nome.upper()}")
        print("=" * 65)
        print(f"{'POS':<4} {'CLUBE':<18} {'PTS':<4} {'V':<3} {'E':<3} {'D':<3} {'SG':<4} {'GP':<3}")
        print("-" * 65)
        for pos, (clube, dados) in enumerate(classificacao_final, start=1):
            saldo = dados["gols_pro"] - dados["gols_contra"]
            print(f"{pos:>2}º  {clube.nome:<18} {dados['pontos']:>3}  {dados['vitorias']:>2}  {dados['empates']:>2}  {dados['derrotas']:>2}  {saldo:>3}  {dados['gols_pro']:>2}")

        print("=" * 65)
        print("⬆️ Série A: mantidos top-16, Z4 rebaixado para Série B.")

    @staticmethod
    def definir_movimentos_serie_a(classificacao_serie_a):
        return {
            "rebaixados": [clube.nome for clube, _ in classificacao_serie_a[-4:]],
            "mantidos": [clube.nome for clube, _ in classificacao_serie_a[:-4]],
        }

    @staticmethod
    def definir_acessos_serie_b(classificacao_serie_b):
        diretos = [clube.nome for clube, _ in classificacao_serie_b[:2]]
        playoff = [clube.nome for clube, _ in classificacao_serie_b[2:6]]
        return {
            "acessos_diretos": diretos,
            "playoff": [(playoff[0], playoff[3]), (playoff[1], playoff[2])],
            "rebaixados_para_c": [clube.nome for clube, _ in classificacao_serie_b[-4:]],
        }
