"""
    Capítulo 10 - Exercícios
"""
# Exercício 10.1 - Time do Vasco
print("============< EXERCÍCIO 10.1 >=============")
with open('aprendendo_python.txt') as arquivo_texto:
    conteudo = arquivo_texto.read()
    print(conteudo.rstrip())

with open('aprendendo_python.txt') as arquivo_texto:
    for linha in arquivo_texto:
        print(linha.rstrip())

with open('aprendendo_python.txt') as arquivo_texto:
    linhas = arquivo_texto.readlines()

for linha in linhas:
    print(linha.rstrip())

# Exercício 10.2 - Substituindo texto
print("============< EXERCÍCIO 10.2 >=============")

with open('aprendendo_python.txt') as arquivo_texto:
    linhas = arquivo_texto.readlines()

for linha in linhas:
    print(linha.replace('Figueiredo', 'Ariel').rstrip())

# Exercício 10.3 - Convidado
print("============< EXERCÍCIO 10.3 >=============")

convidado = input("Digite seu nome: ")
with open('guest.txt', 'w') as arquivo_exerc_10_3:
    arquivo_exerc_10_3.write(convidado)

# Exercício 10.4 - Lista de Convidados
print("============< EXERCÍCIO 10.4 >=============")

with open('guest_book.txt', 'w') as arquivo_exerc_10_4:

    while True:
        convidado = input("Digite seu nome: ")
        if convidado != '':
            arquivo_exerc_10_4.write(convidado + '\n')
        else:
            break

# Exercício 10.6 - Adição
print("============< EXERCÍCIO 10.6 + 10.7 >=============")

print("\nDigite duas parcelas numéricas para soma:")
while True:
    num_01 = input("Primeira parcela: ")
    if num_01 == '':
        break
    num_02 = input("Segunda  parcela: ")
    if num_02 == '':
        break
    try:
        resultado = int(num_01) + int(num_02)
    except ValueError:
        print('Digite valores numéricos ou "" para sair.')
    else:
        print("Resultado = " + str(resultado))

# Exercício 10.8 - Gatos e cachorros
print("============< EXERCÍCIO 10.8 + 10.9 >=============")
arquivos = ['gatos.txt', 'cachorros.txt', 'passaros.txt']

for arquivo in arquivos:
    try:
        with open(arquivo) as arquivo_aberto:
            linhas = arquivo_aberto.readlines()
            print("Nomes no arquivo " + arquivo)
            for linha in linhas:
                print("\t" + linha.rstrip())
    except FileNotFoundError:
        pass
        #print("================================")
        #print("Não existe o arquivo " + arquivo)
        #print("================================")


# Exercício 10.10 - Palavras comuns
print("============< EXERCÍCIO 10.10 >=============")

arquivo = 'WildernessHoney.txt'

try:
    with open(arquivo) as obj_arq:
        conteudo = obj_arq.read()
        contador = conteudo.lower().count('the')
        print("A palavra 'The' aparece " + str(contador) + " vezes.")
except FileNotFoundError:
    pass







