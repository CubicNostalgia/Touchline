from engine.calendario import gerar_calendario
from engine.simulador import simular_partida


class Temporada:
    def __init__(self, liga):
        self.liga = liga

        # Turno (ida)
        self.calendario_turno = gerar_calendario(liga.clubes)

        # Returno (volta) — inverte mando
        self.calendario_returno = [
            [(fora, casa) for casa, fora in rodada]
            for rodada in self.calendario_turno
        ]

        self.tabela = {
            clube: {
                "pontos": 0,
                "vitorias": 0,
                "empates": 0,
                "derrotas": 0,
                "gols_pro": 0,
                "gols_contra": 0,
            }
            for clube in liga.clubes
        }

    # Execução da temporada

    def jogar(self):
        print(f"\n🏁 Início da temporada — {self.liga.nome}\n")

        rodada_global = 1

        # Turno
        for rodada in self.calendario_turno:
            print(f"🕒 Rodada {rodada_global}")

            self._jogar_rodada(rodada)
            rodada_global += 1

        # Returno
        for rodada in self.calendario_returno:
            print(f"🕒 Rodada {rodada_global}")

            self._jogar_rodada(rodada)
            rodada_global += 1

        print("🏁 Fim da temporada\n")
        self.exibir_tabela_final()

    def _jogar_rodada(self, rodada):
        for casa, fora in rodada:
            gols_casa, gols_fora = simular_partida(casa, fora)

            self._registrar_partida(casa, fora, gols_casa, gols_fora)

            print(
                f"  {casa.nome.ljust(12)} {gols_casa} x {gols_fora} {fora.nome}"
            )

        print()

    # Regras da temporada

    def _registrar_partida(self, casa, fora, gols_casa, gols_fora):
        tabela_casa = self.tabela[casa]
        tabela_fora = self.tabela[fora]

        tabela_casa["gols_pro"] += gols_casa
        tabela_casa["gols_contra"] += gols_fora

        tabela_fora["gols_pro"] += gols_fora
        tabela_fora["gols_contra"] += gols_casa

        if gols_casa > gols_fora:
            tabela_casa["vitorias"] += 1
            tabela_casa["pontos"] += 3
            tabela_fora["derrotas"] += 1

        elif gols_casa < gols_fora:
            tabela_fora["vitorias"] += 1
            tabela_fora["pontos"] += 3
            tabela_casa["derrotas"] += 1

        else:
            tabela_casa["empates"] += 1
            tabela_fora["empates"] += 1
            tabela_casa["pontos"] += 1
            tabela_fora["pontos"] += 1

    # Classificação

    def classificacao(self):
        return sorted(
            self.tabela.items(),
            key=lambda item: (
                item[1]["pontos"],
                item[1]["gols_pro"] - item[1]["gols_contra"],
                item[1]["gols_pro"],
            ),
            reverse=True
        )

    def exibir_tabela_final(self):
        print(f"🏆 Classificação Final — {self.liga.nome}")
        print("-" * 55)

        for pos, (clube, dados) in enumerate(self.classificacao(), start=1):
            saldo = dados["gols_pro"] - dados["gols_contra"]

            print(
                f"{pos:2d}º {clube.nome.ljust(12)} "
                f"{dados['pontos']:3d} pts | "
                f"SG {saldo:+3d} | "
                f"G {dados['gols_pro']:2d}"
            )
