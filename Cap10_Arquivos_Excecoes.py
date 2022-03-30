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
