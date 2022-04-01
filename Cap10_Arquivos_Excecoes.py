"""
    Capítulo 10 - Arquivos e Exceções
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('')
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print('')
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print('')
with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + '...')
print(len(pi_string))

aniversario = '17101964'
if aniversario in pi_string:
    print("Seu aniversário em 17/10/1964 está presente em pi.")
else:
    print("Seu aniversário em 17/10/1964 não está presente em pi.")

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    """ O parâmetro 'w' abre um arquivo vazio, mesmo que ele ja´existe o conteudo será apagado. """
    file_object.write('Teste de gravação de arquivo no python.\n')
    file_object.write('Nova linha de arquivo.\n')

with open(filename, 'a') as file_object:
    """ O parâmetro 'a' abre um arquivo para append, mesmo que ele não exista. """
    file_object.write('Acrescentando linhas com o parâmetro "a" na cláusula open.\n')
    file_object.write('Nova linha de arquivo.\n')

try:
    print(5 / 0)
except ZeroDivisionError:
    print("Não pode dividir por zero.")

print("Digite dois numeros e eu vou dividí-los: ")

while True:
    numerador = input("\nNumerador: ")
    if numerador == '':
        break
    denominador = input("Denominador: ")
    if denominador == '':
        break

    try:
        resposta = int(numerador) / int(denominador)
    except ZeroDivisionError:
        print("Divisão inválida.")
    else:
        print("Resposta: ", resposta)


def conta_palavras(arquivo):
    """
    Conta o númer aproximado de palavras em um arquivo
    :param arquivo: Nome do arquivo a ser lido
    :return:
    """
    try:
        with open(filename) as f_obj:
            conteudo = f_obj.read()
    except FileNotFoundError:
        msg = "Desculpe, o arquivo " + filename + ' não existe.'
        print(msg)
    except UnicodeDecodeError:
        msg = "Erro de decodificador de caractaer para o arquivo " + filename
        print(msg)
    else:
        # conta o numero aproximado de palavras no texto #
        palavras = conteudo.split()
        num_palavras = len(palavras)
        print("O arquivo " + filename + " tem aproximadamente " + str(num_palavras) + " palavras.")


filename = 'aprendendo_python.txt'
conta_palavras(filename)

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'siddhartha.txt']
for filename in filenames:
    conta_palavras(filename)


import json

numeros = [2, 3, 5, 7, 11, 13]
filename = 'numeros.json'

with open(filename, 'w') as f_obj:
    json.dump(numeros, f_obj)


filename = 'numeros.json'
with open(filename) as f_obj:
    numeros = json.load(f_obj)
    print(numeros)


def  get_novo_nome_usuario():
    """
    Pede um novo nome de usuário.
    :return:
    """
    filename = 'usuario.json'
    nome_usuario = input("Qual o seu nome? ")
    with open(filename, 'w') as f_obj:
        json.dump(nome_usuario, f_obj)
        return nome_usuario


def get_nome_usuario():
    """
    Obtem o nome do usuário caso já exista
    :return:
    """
    filename = 'usuario.json'
    try:
        with open(filename) as f_obj:
            nome_usuario = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return nome_usuario


def saude_usuario():
    """
    Faz uma saudação ao usuário pelo nome
    :return:
    """
    nome_usuario = get_nome_usuario()
    if nome_usuario:
        print("Bem vindo de volta", nome_usuario + '!')
    else:
        nome_usuario = get_novo_nome_usuario()
        print("Vamos lembrar de você na próxima", nome_usuario + '.')


saude_usuario()
