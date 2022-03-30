"""
    Capítulo 9 - Classes
"""


class Dog():
    """
        Uma tentativa simples de modelar um cachorro
    """

    def __init__(self, name, age):  # Inicializa os atributos name e age
        self.name = name
        self.age = age

    def sit(self):  # Simula um cachorro sentando em resposta a um comando
        print(self.name.title(), 'está sentando agora.')

    def roll_over(self):  # Simula um cachorro rolando em resposta a um comando
        print(self.name.title(), 'está rolando agora.')


my_dog = Dog('Kiara', 7)
your_dog = Dog('Piná', 13)
print("O nome do meu cachorro é", my_dog.name.title() + '.')
print("Meu cachorro tem", str(my_dog.age), 'anos de idade.')
my_dog.sit()
my_dog.roll_over()
print("O nome do seu cachorro é", your_dog.name.title() + '.')
print("Seu cachorro tem", str(your_dog.age), 'anos de idade.')
your_dog.sit()
your_dog.roll_over()


class Carro():
    """
    Uma tentativa simples de representar um carro
    """

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def get_descritivo_nome(self):
        """ Devolve um descritivo do nome do carro formatado """
        nome_completo = str(self.ano) + ' ' + self.marca + ' ' + self.modelo
        return nome_completo.title()

    def leia_odometro(self):
        """ Exibe uma frase que mostra o odometro do carro """
        print("Esse carro tem " + str(self.odometro) + " quilômetros rodados.")

    def atualiza_odometro(self, km):
        """ Atualiza o odometro com o valor especificado,
        rejeitando alteração se valor for menor que atual """
        if km >= self.odometro:
            self.odometro = km
        else:
            print("Não é permitido reduzir o valor do odômetro.")

    def incremente_odometro(self, km):
        if km >= 0:
            self.odometro += km
        else:
            print("Não é permitido reduzir o valor do odômetro.")


class CarroEletrico(Carro):
    """ Apresenta aspectos específicos de carros elétricos """
    def __init__(self, marca, modelo, ano):
        """ Inicializa os atributos da classe pai """
        super().__init__(marca, modelo, ano)
        self.tamanho_bateria = 70

    def descreve_bateria(self):
        """ Exibe uma frase que descreve a capacidade da bateria """
        print("Esse carro tem uma bateria de " + str(self.tamanho_bateria) + '-KWh.')


meu_carro = Carro('chevrolet', 'celta', 2009)
print(meu_carro.get_descritivo_nome())
meu_carro.leia_odometro()
""" ACESSANDO DIRETAMENTE O ATRIBUTO """
meu_carro.odometro = 23
meu_carro.leia_odometro()
""" ATUALIZANDO ATRAVES DE UM MÉTODO """
meu_carro.atualiza_odometro(46)
meu_carro.leia_odometro()
meu_carro.incremente_odometro(4)
meu_carro.leia_odometro()
""" TENTANDO REDUZIR O VALOR DO ODÔMETRO"""
meu_carro.atualiza_odometro(45)
meu_carro.leia_odometro()
meu_carro.incremente_odometro(-3)
meu_carro.leia_odometro()
meu_tesla = CarroEletrico('tesla', 'model s', 2022)
print(meu_tesla.get_descritivo_nome())
meu_tesla.descreve_bateria()

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

