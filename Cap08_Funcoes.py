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
