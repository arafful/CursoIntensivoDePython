"""
    Exercícios Capítulo 4
"""
# 4.1 - Pizzas
pizzas = ["peperoni", "marguerita", "calabreza"]

for pizza in pizzas:
    print("Vamos pedir uma pizza grande de", pizza.title())

print("\nPizza tem que ser grande e com borda recheada.\n\n")

# 4.2 - Animais
bichos = ["papagaio", "gato", "cachorro"]

for bicho in bichos:
    print("Um", bicho, "seria um ótimo animal de estimação.")

print("\nEu gosto de ter pets.\n\n")

# 4.3 - Contando até 20
for i in range(1, 21):
    print(i)
print("\n")

# 4.4 - Um milhão
numeros = range(1, 1000001)
#for numero in numeros:
#    print(numero)

# 4.5 - Somando um milhão
print(min(numeros))
print(max(numeros))
print(sum(numeros))

# 4.6 - Números ímpares
impares = range(1, 20, 2)
for i in impares:
    print(i)

# 4.7 - Múltiplos de 3
multiplos = [i * 3 for i in range(1, 11)]
for i in multiplos:
    print(i)

# 4.8 - Cubos - com for
cubos = []
for i in range(1,11):
    cubos.append(i ** 3)

print(cubos)

# 4.9 - Cubos - Comprehension
cubos = [i ** 3 for i in range(1, 11)]
for i in cubos:
    print(i)

# 4.10 - Fatias
jogadores = ["Mazaropi", "Orlando", "Abel", "Geraldo", "Marco Antonio", "Zé Mario", "Zanata", "Dirceu", "Wilsinho",
             "Roberto", "Ramon"]
print("Os defensores do meu time são:", jogadores[: 5])
print("Os meias são:", jogadores[5:8])
print("Os atacantes são:", jogadores[8:])

# 4.11 - Minhas Pizzas e Suas Pizzas
suas_pizzas = pizzas[:]
pizzas.append("Aliche")
suas_pizzas.append("Romana")
print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)

print("Suas pizzas preferidas são:")
for pizza in suas_pizzas:
    print(pizza)

print("\n")

# 4.13 - Buffet - TUPLAS
pratos = ("Virado Paulista", "Macarronada", "Feijoada", "Cozido", "Estrogonofe")
for prato in pratos:
    print(prato)

print("\n")

pratos = ("Filé com fritas", "Macarronada", "Leitão a pururuca", "Cozido", "Estrogonofe")
for prato in pratos:
    print(prato)

print("\n")
