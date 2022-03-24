"""
    Capítulo 7 - Exercicios
"""
# 7.1 - Locação de automoveis

print("\n#### Exercício 7.1 ####")
carro = input("Qual marca de carro gostaria de alugar? ")
print("Deixe-me ver se consigo um", carro, "para você.")

# 7.2 - Lugares em restaurante

print("\n#### Exercício 7.2 ####")
lugares = int(input("Mesa para quantas pessoas? "))

if lugares >= 8:
    print("Por favor, aguardem a disponibilidade da mesa.")
else:
    print("Sua mesa está disponível.")

# 7.3 - Múltiplo de 10

print("\n#### Exercício 7.3 ####")
numero = int(input("Digite um número: "))

if (numero % 10) == 0:
    print(str(numero), "é múltiplo de 10.")
else:
    print(str(numero), "não é múltiplo de 10.")

# 7.4 - Ingredientes para uma pizza

print("\n#### Exercício 7.4 ####")
prompt = "Digite os ingredientes para sua pizza.\nDigite quite para encerrar."
ingrediente = ""

while ingrediente != "quit":
    ingrediente = input(prompt)
    if ingrediente != "quit":
        print("Acrescentamos", ingrediente, "na sua pizza.")
