"""
    Capítulo 11
"""
from Cap11_name_function import get_nome_formatado

print("Entre 'q' a qualquer momento para finalizar.")

while True:
    nome = input("\nPor favor, digite um nome: ")
    if nome == 'q':
        break
    sobrenome = input("Por favor, digite um sobrenome: ")
    if sobrenome == 'q':
        break
    nome_completo = get_nome_formatado(nome, sobrenome)
    print("Nome formatado é", nome_completo + '.')
