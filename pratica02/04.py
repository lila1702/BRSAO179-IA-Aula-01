# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
distancia = 300 #km
combustivel_gasto = 25 #litros

consumo_medio = distancia / combustivel_gasto

print(f"A viagem de {distancia} km, com {combustivel_gasto} L gastos, teve consumo médio de {consumo_medio:.2f} km/L")