"""
    Exercícios - Capítulo 4
"""
# 5.1 - Testes condicionais
carro = "celta"
print("Carro é igual a Celta? ", (carro == "celta"))
print("Carro é igual a Onix? ", (carro == "onix"))

# 5.2 - Mais testes condicionais
print("Carro é CORSA? ", (carro.upper() == "CELTA"))

num_01 = 23
num_02 = 38
if num_01 > 20 and num_02 <= 40:
    print("Correto")

carros = ["palio", "clio", "corolla", "celta"]
if "palio" in carros:
    print("palio está na lista.\n")

if "fusca" not in carros:
    print("Fusca não está na lista.\n")

# 5.3 - Cores de alienigenas #1
#alien_color = "green"
alien_color = "yellow"
#alien_color = "red"

if alien_color == "green":
    print("Você acabou de ganhar 5 pontos.\n")

# 5.4 - Cores de alienigenas #2
alien_color = "green"
#alien_color = "yellow"
#alien_color = "red"

if alien_color == "green":
    print("Você ganhou 5 pontos por atingir o alienigena.\n")
else:
    print("Você acabou de ganhar 10 pontos.\n")

# 5.5 - Cores de alienigenas #3
#alien_color = "green"
#alien_color = "yellow"
alien_color = "red"

if alien_color == "green":
    pontos = 5
elif alien_color == "yellow":
    pontos = 10
elif alien_color == "red":
    pontos = 15

print("Você ganhou", str(pontos), "pontos.\n")

# 5.6 - Estágios da vida
idade = int(input("Qual a idade? "))

if idade < 2:
    estagio = "um bebê"
elif idade < 4:
    estagio = "uma criança"
elif idade < 13:
    estagio = "um(a) garoto(a)"
elif idade < 20:
    estagio = "um adolescente"
elif idade < 65:
    estagio = "um adulto"
elif idade >= 65:
    estagio = "um idoso"

print("Você é", estagio)

# 5.7 - Fruta favorita
frutas = ["banana", "maçã", "figo"]
if "banana" in frutas:
    print("Bananas são boas e baratas.")

if "figo" in frutas:
    print("Eu prefiro figos.")

if "maçã" in frutas:
    print("Maçãs são as preferidas dos médicos.\n")

# 5.8 - Olá admin
usuarios = ["admin", "andre", "monica", "felipe", "elen", "luiza"]

if usuarios: ### LINHA INCLUÍDA PARA O EXERCÍCIO 5.9 ###
    for usuario in usuarios:
        if usuario == "admin":
            print("Olá admin! Gostaria de acessar um relatório de status?")
        else:
            print("Olá", usuario.title() + ", obrigado por fazer login novamente.")

# 5.9 Sem usuários
##### LINHA INCLUÍDA NA SOLUÇÃO DO 5.8

# 5.10 Verificando nomes de usuários
usuarios_existentes = ["jose", "joaquim", "manoel", "francisco", "maria", "luiza"]
novos_usuarios = ["fabricio", "lucio", "alexandre", "francisco", "marcos", "maria"]

if novos_usuarios:
    for novo in novos_usuarios:
        if novo.lower() not in usuarios_existentes:
            print("Nome de usuário disponivel para", novo.title())
        else:
            print(novo.title() + ", esse nome já está em uso.")

# 5.11 - Números ordinais
ordinais = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal in ordinais:
    if ordinal == 1:
        print("1st")
    elif ordinal == 2:
        print("2nd")
    elif ordinal == 3:
        print("3rd")
    else:
        print(str(ordinal) + "th")


