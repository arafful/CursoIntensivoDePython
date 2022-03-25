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
