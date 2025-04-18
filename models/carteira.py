from .transacao import Transacao

class Carteira:
    def __init__(self):
        self.transacoes: list[Transacao] = []

    def adicionar(self, transacao: Transacao):
        self.transacoes.append(transacao)

    def exibir_transacoes(self):
        print("\n--- Histórico de Transações ---")
        for transacao in self.transacoes:
            print(transacao.resumo())
        print("-------------------------------")

    def saldo(self) -> float:
        return sum(t.valor for t in self.transacoes)

    def filtrar_por_categoria(self, categoria: str):
        print(f"\n--- Transações da categoria: {categoria} ---")
        for t in self.transacoes:
            if t.categoria.lower() == categoria.lower():
                print(t.resumo())
        print("-------------------------------------------")

    def gastos_totais(self) -> float:
        return sum(t.valor for t in self.transacoes if t.valor < 0)

    def renda_total(self) -> float:
        return sum(t.valor for t in self.transacoes if t.valor > 0)

    def resumo_geral(self):
        print("\n===== RESUMO GERAL =====")
        print(f"Total de transações: {len(self.transacoes)}")
        print(f"Renda total: +{self.renda_total():.2f}")
        print(f"Gastos totais: {self.gastos_totais():.2f}")
        print(f"Saldo final: {self.saldo():.2f}")
        print("=========================")
