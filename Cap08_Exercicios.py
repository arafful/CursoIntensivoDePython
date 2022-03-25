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

