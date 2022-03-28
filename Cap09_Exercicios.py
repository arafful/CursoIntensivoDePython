"""
    Capítulo 9 - Exercícios
"""
# Exercício 9.1 - Restaurante
print("============< EXERCICIO 9.1 >=============")


class Restaurante():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def descreva_restaurante(self):
        print(self.nome.title(), "é um restaurante de cozinha do tipo", self.tipo.title())

    def abra_restaurante(self):
        print("O restaurante", self.nome.title(), "está aberto.")


restaurante = Restaurante('edu bar de minas', 'comida mineira')
restaurante.descreva_restaurante()
restaurante.abra_restaurante()

# Exercício 9.2 - Três restaurantes
print("============< EXERCICIO 9.2 >=============")

rest_01 = Restaurante('damasco', 'árabe')
rest_02 = Restaurante('japa one', 'japonês')
rest_03 = Restaurante('burger king', 'lanches')
rest_01.descreva_restaurante()
rest_02.descreva_restaurante()
rest_03.descreva_restaurante()

# Exercício 9.3 - Usuários
print("============< EXERCICIO 9.3 >=============")


class Usuario():
    def __init__(self, nome, sobrenome, sexo, idade, tipo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.idade = idade
        self.tipo = tipo

    def descreva_usuario(self):
        print("Dados do usuário:", self.nome.title())
        print("\tSobrenome:", self.sobrenome.title())
        print("\tSexo:", self.sexo.title())
        print("\tIdade:", str(self.idade))
        print("\tTipo:", self.tipo.title())

    def saude_usuario(self):
        print("Olá", self.nome.title() + '.')


user01 = Usuario('andré', 'rafful', 'masculino', 57, 'pai')
user02 = Usuario('mônica', 'pedrosa', 'feminino', 52, 'mãe')
user03 = Usuario('felipe', 'rafful', 'masculino', 33, 'filho')
user04 = Usuario('luiza', 'hassad', 'feminino', 27, 'filha')
#
user01.descreva_usuario()
user02.descreva_usuario()
user03.descreva_usuario()
user04.descreva_usuario()
#
user01.saude_usuario()
user02.saude_usuario()
user03.saude_usuario()
user04.saude_usuario()
