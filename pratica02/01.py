# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
def converte_moeda(valor, taxa):
    return valor / taxa

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

print(f"O valor de R$ {valor_reais} convertido para dólar é $ {converte_moeda(valor_reais, taxa_dolar):.2f}")
print(f"O valor de R$ {valor_reais} convertido para euro é € {converte_moeda(valor_reais, taxa_euro):.2f}")

print("Oi")
# Lila: Meu Deus, eu tô me sentindo pobre. 100 reais é quase trocado pra eles