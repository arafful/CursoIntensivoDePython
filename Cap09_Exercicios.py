"""
    Capítulo 9 - Exercícios
"""
# Exercício 9.1 - Restaurante
print("============< EXERCICIO 9.1 >=============")


class Restaurante():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.atendidos = 0

    def descreva_restaurante(self):
        print(self.nome.title(), "é um restaurante de cozinha do tipo", self.tipo.title())

    def abra_restaurante(self):
        print("O restaurante", self.nome.title(), "está aberto.")

    def set_atendidos(self, numero):
        self.atendidos = numero

    def incremente_atendidos(self, numero):
        self.atendidos += numero


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
        self.tentativas_login = 0

    def descreva_usuario(self):
        print("Dados do usuário:", self.nome.title())
        print("\tSobrenome:", self.sobrenome.title())
        print("\tSexo:", self.sexo.title())
        print("\tIdade:", str(self.idade))
        print("\tTipo:", self.tipo.title())

    def saude_usuario(self):
        print("Olá", self.nome.title() + '.')

    def incremente_tentativas_login(self):
        self.tentativas_login += 1

    def reset_tentativas_login(self):
        self.tentativas_login = 0


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

# Exercício 9.4 - Pessoas atendidas
print("============< EXERCICIO 9.4 >=============")

rest_9_4 = Restaurante('esquina', 'barzinho')
rest_9_4.descreva_restaurante()
print(rest_9_4.atendidos)
rest_9_4.atendidos = 9
print(rest_9_4.atendidos)
rest_9_4.set_atendidos(10)
print(rest_9_4.atendidos)
rest_9_4.incremente_atendidos(2)
print(rest_9_4.atendidos)

# Exercício 9.5 - Tentativas de login
print("============< EXERCICIO 9.5 >=============")

user01.incremente_tentativas_login()
print(user01.tentativas_login)
user01.incremente_tentativas_login()
print(user01.tentativas_login)
user01.incremente_tentativas_login()
print(user01.tentativas_login)
user01.incremente_tentativas_login()
print(user01.tentativas_login)
user01.reset_tentativas_login()
print(user01.tentativas_login)



