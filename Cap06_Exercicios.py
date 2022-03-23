"""
    Capítulo 6 - Exercícios
"""
# 6.1 - Pessoa
pessoa = {'nome': 'andré', 'sobrenome': 'rafful', 'idade': 58}

print("\nExercício 6.1")
print("Nome:", pessoa['nome'].title())
print("Sobrenome:", pessoa['sobrenome'].title())
print("Idade:", str(pessoa['idade']))

# 6.2 - Números Favoritos
numeros_favoritos = {'andre': 10, 'luiz': 20, 'figueiredo': 30, 'rafful': 40}

print("\nExercício 6.2")
for i in numeros_favoritos:
    print("O número favorito de", i.title(), "é", str(numeros_favoritos[i]) + '.')

# 6.2 - Glossário
glossario = {
    'argumento': 'Um valor passado para uma função (ou método) ao chamar a função.',
    'classe': 'Um modelo para criação de objetos definidos pelo usuário.',
    'docstring': 'Abreviatura de “documentation string” (string de documentação).'
}

print("\nExercício 6.3")
for i in glossario:
    print(i.title(), "\t-\t", glossario[i])
