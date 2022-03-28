"""
    Capítulo 8 - Exercícios
"""
# 8.1 - Mensagens

print("===< EXERCÍCIO 8.1 >===")


def display_message():
    print("Capitulo 8 - Funções")


display_message()

# 8.2 - Livros
print("\n===< EXERCÍCIO 8.2 >===")


def livro_favorito(nome_livro):
    print('O meu livro favorito é: "' + nome_livro + '".')


livro_favorito("O Caso dos Dez Negrinhos")

# 8.3 - Camisetas
print("\n===< EXERCÍCIO 8.3 >===")


def make_shirt(tamanho, texto):
    print('\nO tamanho da camiseta será', tamanho + ',')
    print('e a frase será:', texto + '.')


make_shirt('GG', 'Salvem as baleias')
make_shirt(tamanho='P', texto='O sentimento não pode parar')

# 8.4 - Camisetas Grandes
print("\n===< EXERCÍCIO 8.4 >===")


def make_shirt2(tamanho='G', texto='Eu amo Python'):
    print('\nO tamanho da camiseta será', tamanho + ',')
    print('e a frase será:', texto + '.')


make_shirt2()
make_shirt2(tamanho='P')
make_shirt2(tamanho='M')
make_shirt2(texto='C++ já era')

# 8.5 - Cidades
print("\n===< EXERCÍCIO 8.5 >===")


def describe_city(nome_cidade, pais_cidade='Brasil'):
    print('\nCidade:', nome_cidade.title(), '- País:', pais_cidade.title() + ',')

describe_city('rio de janeiro')
describe_city('campinas')
describe_city('New York', 'USA')
describe_city(nome_cidade='méxico', pais_cidade='méxico')

# 8.6 - Nomes de Cidades
print("\n===< EXERCÍCIO 8.6 >===")


def city_country(city_name, country_name):
    print(city_name.title() + ' , ' + country_name.title())


city_country('rio de janeiro', 'brasil')
city_country('campinas', 'brasil')
city_country('Buenos Aires', 'argentina')

# 8.7 - Albúm
print("\n===< EXERCÍCIO 8.7 >===")


def make_album(artista, nome_album, num_faixas=''):
    album = {'artista': artista.title(), 'album': nome_album.title()}
    if num_faixas:
        album['faixas'] = num_faixas
    return album


print(make_album('madona', 'imaculate colection'))

# 8.8 - Albúns dos usuários
print("\n===< EXERCÍCIO 8.8 >===")

meus_albuns = []
while True:
    print("Digite a lista de seus albúns favoritos.\ndigite 'q' para sair.")
    nome_artista = input("Artista: ")
    if nome_artista == 'q':
        break
    nome_album = input("Álbum: ")
    if nome_album == 'q':
        break

    meus_albuns.append(make_album(nome_artista, nome_album))

for album in meus_albuns:
    print(album)

# 8.9 - Mágicos
print("\n===< EXERCÍCIO 8.9 >===")


def show_magicians(magicos):
    for magico in magicos:
        print(magico.title())


magicos = ['andre rafful', 'monica pedrosa', 'felipe hassad rafful', 'luiza hassad pedrosa']
show_magicians(magicos)

# 8.10 - Grandes Mágicos
print("\n===< EXERCÍCIO 8.9 >===")


def make_great(magicos):
    new_magicians = []
    for magico in magicos:
        new_magicians.append("Great " + magico)

    return new_magicians


magicos = ['andre rafful', 'monica pedrosa', 'felipe hassad rafful', 'luiza hassad pedrosa']
novos_magicos = make_great(magicos)
show_magicians(novos_magicos)
show_magicians(novos_magicos)


