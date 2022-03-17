"""
    Capítulo 3 - Listas
"""
bicicletas = ["Canadian", "Trek", "Specialized", "Cannondale"]
print(bicicletas)
print(bicicletas[0])
print(bicicletas[0].upper())
print(bicicletas[1])
print(bicicletas[3])
print(bicicletas[-1])

mensagem = "Minha primeira bicicleta foi uma " + bicicletas[0]
print(mensagem)

motos = ["honda", "yamaha", "susuki"]
print(motos)
motos[0] = "ducati"
print(motos)

motos = ["honda", "yamaha", "susuki"]
print(motos)
motos.append("ducati")
print(motos)

motos_novas = []
motos_novas.append("honda")
motos_novas.append("yamaha")
motos_novas.append("susuki")
print(motos_novas)

motos_novas.insert(0, "ducati")
print(motos_novas)

del motos_novas[0]
print(motos_novas)

print(motos)

poped_motos = motos.pop()
print(poped_motos)
print(motos)

motos = ["honda", "yamaha", "susuki", "ducati"]
print(motos)
motos.remove("ducati")
print(motos)

carros = ["bmw", "audi", "toyota", "subaru"]
print("Aqui está a lista original:")
print(carros)
print("\nAqui está a lista ordenada:")
print(sorted(carros))
print("\nAqui está a lista original de novo:")
print(carros)
carros.sort()
print(carros)
carros.sort(reverse=True)
print(carros)

carros = ["bmw", "audi", "toyota", "subaru"]
carros.reverse()
print(carros)
carros.reverse()
print(carros)

print(len(carros))
