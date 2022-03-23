"""
    Capítulo 6 - Dicionários
"""
alien_0 = {"cor": "verde", "pontos": 5}
print(alien_0["cor"])
print(alien_0["pontos"])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Começando um dicionário vazio

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print("The alien is", alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is", alien_0['color'] + ".")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['color'] = 'green'
alien_0['points'] = 5
print("Original x-position: ", str(alien_0['x_position']))
# Move o alienigena para a direita
# Determina a distância que o alienigena deve se deslocar de acordo com sua velocidade atual

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser o alienigena rápido
    x_increment = 3

# A nova posição é a posição antiga mais o incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: ", str(alien_0['x_position']))

print(alien_0)
del alien_0['points']
print(alien_0)

linguagens_favoritas = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

print('A linguagem favorita da Sarah é', linguagens_favoritas['sarah'].title() + '.')





