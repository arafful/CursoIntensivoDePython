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
