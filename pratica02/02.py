# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)

print(f"Produto: {nome_produto} | Valor: {preco_original:.2f}\nDesconto: {valor_desconto:.2f} ({porcentagem_desconto}%) | Valor Final: {(preco_original - valor_desconto):.2f}")