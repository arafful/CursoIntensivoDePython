"""
    Capítulo 4 - Trabalhando com Listas
"""
magicos = ["alice", "david", "carolina"]

for magico in magicos:
    print((magico.title()), "parabéns, grande truque.")
    print("Mal posso esperar pelo próximo truque!\n")

print("Obrigado a todos vocês, foi um ótimo show de mágicas.")

for i in range(1, 5):
    print(i)
print("\n")

numeros = list(range(1, 6))
for numero in numeros:
    print(numero)
print("\n")

numeros_pares = list(range(2, 11, 2))
for par in numeros_pares:
    print(par)
print("\n")

quadrados = []
for i in range(1, 11):
    quadrados.append(i ** 2)

print(quadrados)
print("\n")
