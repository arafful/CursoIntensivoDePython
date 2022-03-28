"""
    Capítulo 8 - Funções
"""


# Exibe uma saudação simples
def saudacao_usuario(nome_usuario):
    print("Olá", nome_usuario.title() + '.')


saudacao_usuario('andre')
saudacao_usuario('monica')


def descreve_pet(tipo_animal='cachorro', nome_animal=''):
    print("\nEu tenho um", tipo_animal + '.')
    print('Meu', tipo_animal, 'se chama', nome_animal.title() + '.')


descreve_pet('pit bull', 'kiara')
descreve_pet('vira-lata', 'piná')
descreve_pet('dushround', 'xuxa')

descreve_pet(nome_animal='kiara', tipo_animal='pit bull')

descreve_pet(nome_animal='Kiara')


def nome_formatado(nome, sobrenome):
    # Retorna um nome completo, formatado de forma elegante.
    nome_completo = nome + ' ' + sobrenome
    return nome_completo.title()


magico = nome_formatado('andré', 'rafful')
print('\n' + magico)


def build_person(first_name, last_name, age=''):
    # Devolve um dicionário com informações sobre uma pessoa
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix', age=27)
print(musician)


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print('\nPlease tell me your name:')
    print("Enter 'q' at any time to exit.")
    fname = input("First name: ")
    if fname == 'q':
        break
    lname = input("Last name: ")
    if lname == 'q':
        break
    formatted_name = get_formatted_name(fname, lname)
    print("\nHello", formatted_name + '!')


def greet_users(names):
    # Exibe uma saudação simples a cada usuário da lista
    for name in names:
        print("Olá,", name.title() + '!')


usernames = ['andre', 'luiz', 'figueiredo', 'rafful']
greet_users(usernames)

# printing models
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model:" + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:" + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['capa de iphone', 'robô aspirador', 'qualquer porra']
completed_models = []
print_models(unprinted_designs)
show_completed_models(completed_models)

# Usando uma função de módulo externo
import Cap08_Modulo_Funcoes
Cap08_Modulo_Funcoes.make_pizza(16, 'pepperoni')
Cap08_Modulo_Funcoes.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importando apenas uma funçao com alias
from Cap08_Modulo_Funcoes import make_pizza as mp
mp(16, 'calabresa')
mp(12, '4 queijos', 'aliche', 'oregano')

# Usando alias para o nome do Módulo
import Cap08_Modulo_Funcoes as f
f.make_pizza(16, 'napolitana')
f.make_pizza(12, 'cebola', 'bacon', 'azeitona')
