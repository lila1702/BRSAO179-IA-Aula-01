print("BEM VINDO À COPA RELÂMPAGO PELO PRIMEIRO LUGAR NA CORRIDA DO MARIO KART\nEscolha seu personagem:")
opcoes = ["Mario", "Luigi", "Yoshi", "Princesa Peach", "King Boo", "Bowser", "Princesa Daisy", "Princesa Rosalina"]

for i in range(len(opcoes)):
    print(f"Digite {i} para {opcoes[i]}")

print()
user_choice = int(input())
print(f"Você escolheu {opcoes[user_choice]}")