# 4- Calculadora de Preço Total
# * Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# * Nome do produto: "Cadeira Infantil"
# * Preço unitário: R$ 12.40
# * Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

nome_produto = "Cadeira Infantil"
preco = 12.40
qtd = 3
preco_total = preco * qtd
print(f"{nome_produto} | R$ {preco} | {qtd} unidade(s) | Valor Total: R$ {preco_total:.2f}")