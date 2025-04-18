# 💸 Carteira Virtual - Controle Financeiro Pessoal com POO

Este é um projeto simples de **controle financeiro pessoal** feito em Python, utilizando os princípios de **Programação Orientada a Objetos (POO)**.

## 🚀 Funcionalidades

- Adicionar transações (entrada e saída de dinheiro)
- Categorizar as transações (ex: Renda, Alimentação, Moradia)
- Exibir histórico financeiro
- Filtrar transações por categoria
- Exibir resumo geral com renda, gastos e saldo final

## 📦 Estrutura do Projeto

carteira_virtual/
├── main.py
├── models/
│   ├── init.py
│   ├── transacao.py
│   └── carteira.py
├── .gitignore
└── README.md


## 🛠️ Como executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Joaoapbrito1/Desafio-01-Python.git](https://github.com/Joaoapbrito1/Desafio-01-Python.git)

Execute o script principal:
Bash

python main.py
Requisitos: Python 3.7 ou superior
📋 Exemplo de saída
Markdown

--- Histórico de Transações ---
Salário     | +3000 | Renda       | 01/04/2025
Supermercado |  -250 | Alimentação | 03/04/2025
Aluguel     | -1200 | Moradia     | 05/04/2025
Freelance   |  +800 | Renda       | 10/04/2025
Restaurante |   -90 | Alimentação | 12/04/2025
-------------------------------

===== RESUMO GERAL =====
Total de transações: 5
Renda total: +3800.00
Gastos totais: -1540.00
Saldo final: 2260.00
=========================

--- Transações da categoria: Alimentação ---
Supermercado |  -250 | Alimentação | 03/04/2025
Restaurante |   -90 | Alimentação | 12/04/2025
-------------------------------------------
✨ Tecnologias utilizadas
Python 3
Programação Orientada a Objetos (POO)
📄 Licença
Este projeto está sob a licença MIT.