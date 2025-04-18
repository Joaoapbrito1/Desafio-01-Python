from models.transacao import Transacao
from models.carteira import Carteira

def main():
    carteira = Carteira()

    carteira.adicionar(Transacao("Salário", 3000, "Renda", "01/04/2025"))
    carteira.adicionar(Transacao("Supermercado", -250, "Alimentação", "03/04/2025"))
    carteira.adicionar(Transacao("Aluguel", -1200, "Moradia", "05/04/2025"))
    carteira.adicionar(Transacao("Freelance", 800, "Renda", "10/04/2025"))
    carteira.adicionar(Transacao("Restaurante", -90, "Alimentação", "12/04/2025"))

    carteira.exibir_transacoes()
    carteira.resumo_geral()
    carteira.filtrar_por_categoria("Alimentação")

if __name__ == "__main__":
    main()
