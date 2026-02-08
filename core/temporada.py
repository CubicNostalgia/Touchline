from engine.calendario import gerar_calendario
from engine.simulador import simular_partida
from ui.mensagens import mensagem_fim_temporada

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

        # Calendário completo (ida + volta)
        self.calendario_completo = self.calendario_turno + self.calendario_returno

        self.rodada_atual = 0  # índice da rodada

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

    # ======================
    # Execução da temporada
    # ======================

    def simular_proxima_rodada(self):
        if self.rodada_atual >= len(self.calendario_completo):
            print("\n🏁 A temporada já terminou.\n")
            return False

        rodada = self.calendario_completo[self.rodada_atual]
        numero_rodada = self.rodada_atual + 1

        print(f"\n🕒 Rodada {numero_rodada}")
        self._jogar_rodada(rodada)

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
            
            # Alinhamento dos resultados das partidas
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
        elif gols_casa < gols_fora:
            t_fora["vitorias"] += 1
            t_fora["pontos"] += 3
            t_casa["derrotas"] += 1
        else:
            t_casa["empates"] += 1
            t_fora["empates"] += 1
            t_casa["pontos"] += 1
            t_fora["pontos"] += 1

    # ======================
    # Classificação e Tabela
    # ======================

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
        # Limpa a tela ou garante que só rode uma vez
        classificacao_final = self.classificacao()

        print(f"\n🏆 CLASSIFICAÇÃO FINAL — {self.liga.nome.upper()}")
        print("=" * 65)
        print(f"{'POS':<4} {'CLUBE':<18} {'PTS':<4} {'V':<3} {'E':<3} {'D':<3} {'SG':<4} {'GP':<3}")
        print("-" * 65)

        for pos, (clube, dados) in enumerate(classificacao_final, start=1):
            saldo = dados["gols_pro"] - dados["gols_contra"]
            # Usamos o nome do clube diretamente para evitar repetições de IDs
            nome_clube = clube.nome
            
            print(f"{pos:>2}º  {nome_clube:<18} "
                  f"{dados['pontos']:>3}  "
                  f"{dados['vitorias']:>2}  "
                  f"{dados['empates']:>2}  "
                  f"{dados['derrotas']:>2}  "
                  f"{saldo:>3}  "
                  f"{dados['gols_pro']:>2}")

        print("=" * 65)

        print("=" * 65)
        
        # Opcional: Mostrar veredito do G4 e Z4 usando o ui/mensagens.py
        # Aqui, como não sabemos qual clube é o do usuário nesta classe, 
        # apenas identificamos as zonas.
        print("\nℹ️  Zonas de Classificação:")
        print(f"• 1º a 4º: Fase de Grupos Libertadores")
        print(f"• 5º: Pré-Libertadores")
        print(f"• 17º a 20º: Rebaixamento")