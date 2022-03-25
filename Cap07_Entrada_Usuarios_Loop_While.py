"""
    Capítulo 7 - Entrada de usuários e loops while
"""
mensagem = ""
prompt = "Diga-me alguma coisa e eu repetirei para você:\nDigite quit para sair."
active = True

while active:
    mensagem = input(prompt)
    if mensagem == "quit":
        active = False
    else:
        print(mensagem)

mensagem = input("Digite seu nome: ")
print("Olá", mensagem + "!")

prompt = "Se você nos disser quem você é, nós poderemos personalizar as suas mendagens."
prompt += "\nQual o seu primeiro nome? "
name = input(prompt)
print("\nOlá", name + "!")

idade = int(input("Qual a sua idade? "))
print(idade >= 18)

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

usuarios_confirmados = []
usuarios_nao_confirmados = ['alice', 'brian', 'candance']

# Confirma cada usuário, até que não haja mais usuários não confirmados

while usuarios_nao_confirmados:
    usuario_corrente = usuarios_nao_confirmados.pop()
    print("Verificando usuário:", usuario_corrente.title())
    usuarios_confirmados.append(usuario_corrente)

# Exibe todos os usuários confirmados
print("\nOs seguintes usuários foram confirmados:")
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.title())

print(usuarios_nao_confirmados)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

respostas = {}
ativo = True

while ativo:
    # Pede o nome e a resposta da pesquisa
    nome = input("\nQual o seu nome? ")
    resposta = input("Para qual time você torce? ")
    # Armazena a resposta da pesquisa em um dicionário
    respostas[nome] = resposta
    # Verifica se mais alguém vai responder a pesquisa
    flag = input("Mais alguém vai responder a pesquisa? (Sim/Não")
    if flag != 'Sim':
        ativo = False

# Mostra o resultado da pesquisa
for nome, resposta in respostas.items():
    print(nome, "torce pelo", resposta + '.')


