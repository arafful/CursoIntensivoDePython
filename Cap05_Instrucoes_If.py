"""
    Instruções if
"""
carros = ["audi", "bmw", "subaru", "honda", "toyota"]
for carro in carros:
    if carro == "bmw":
        print(carro.upper())
    else:
        print(carro.title())

print("\n")

if "audi" in carros:
    print("Audi faz parte da lista.\n")

if "kia" not in carros:
    print("Kia pode ser incluído na lista de carros.\n")

idade = 18
#idade = 17
if idade >= 18:
    print("Você tem idade suficiente para votar.")
    print("Você já sabe o seu local de votação?\n")
else:
    print("Você não tem idade suficiente para votar.")
    print("Aguarde a idade regulamentada para fazer seu cadastro.\n")

idade = 12
#idade = 66
#idade = 3
if idade < 4:
    preco = 0
elif idade >= 18:
    preco = 10
else:
    preco = 5

print("Seu ingresso custa R$:", str(preco), "\n")

idade = 12
#idade = 66
#idade = 3
if idade < 4:
    preco = 0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
else:
    preco = 5

print("Seu ingresso custa R$:", str(preco), "\n")

ingredientes = ["cogumelos", "pimentão verde", "queijo extra"]
#ingredientes = []

if ingredientes:
    for ingrediente in ingredientes:
        if ingrediente == "pimentão verde":
            print("Lamentamos, mas estamos sem pimentões verdes.")
        else:
            print("Adicionando", ingrediente + ".")
else:
    print("Tem certeza que deseja uma pizza simples?")

print("Sua pizza está pronta.\n")

# LISTAS RELACIONADAS
ingredientes_disponiveis = ["cogumelo", "peperoni", "calabresa", "aliche", "presunto", "palmito", "tomate seco"]
ingredientes_solicitados = ["cogumelo", "batata frita", "aliche"]

for ingrediente_solicitado in ingredientes_solicitados:
    if ingrediente_solicitado in ingredientes_disponiveis:
        print("Adicionando", ingrediente_solicitado + ".")
    else:
        print("Lamentamos, mas não temos", ingrediente_solicitado +".")

print("Sua pizza está pronta.\n")
