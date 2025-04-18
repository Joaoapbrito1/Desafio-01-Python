class Transacao:
    def __init__(self, descricao: str, valor: float, categoria: str, data: str):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data

    def resumo(self) -> str:
        sinal = "+" if self.valor >= 0 else "-"
        return f"{self.descricao} | {sinal}{abs(self.valor)} | {self.categoria} | {self.data}"