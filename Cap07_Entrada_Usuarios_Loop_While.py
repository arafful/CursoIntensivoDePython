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
