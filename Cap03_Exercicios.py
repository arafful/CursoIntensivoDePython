# 3.1 - Nomes
nomes_amigos = ["Wanderley", "Zé Roberto", "Gurjão", "Carlão", "Márcio"]
print(nomes_amigos[0])
print(nomes_amigos[1])
print(nomes_amigos[2])
print(nomes_amigos[3])
print(nomes_amigos[4])

# 3.2 - Saudações
mensagem = "Olá meu amigo " + nomes_amigos[0]
print(mensagem)
mensagem = "Olá meu amigo " + nomes_amigos[1]
print(mensagem)
mensagem = "Olá meu amigo " + nomes_amigos[2]
print(mensagem)
mensagem = "Olá meu amigo " + nomes_amigos[3]
print(mensagem)
mensagem = "Olá meu amigo " + nomes_amigos[4]
print(mensagem)

# 3.3 - Sua própria lista
praias = ["Saquarema", "Jaconé", "Arraial do Cabo", "Cabo Frio", "Búzios"]
frases = ["Gostaria de morar em ", "Adoro a praia de ", ]

# 3.4 - Lista de convidados
convidados = ["Mônica", "Felipe", "Luiza"]
mensagem = ", você está convidado(a) para um jantar às 20 horas."
print(convidados[0], mensagem)
print(convidados[1], mensagem)
print(convidados[2], mensagem)

# 3.5 - Alterando a lista de convidados
del convidados[1]
convidados.append("Lula")
print(convidados[0], mensagem)
print(convidados[1], mensagem)
print(convidados[2], mensagem)

# 3.6 - Mais convidados
print("Encontramos uma mesa de jantar maior.")
convidados.insert(0, "Fátima")
convidados.insert(2, "Adriana")
convidados.insert(-1, "Felipe")
print(convidados[0], mensagem)
print(convidados[1], mensagem)
print(convidados[2], mensagem)
print(convidados[3], mensagem)
print(convidados[4], mensagem)
print(convidados[5], mensagem)
print("Agora somos ", len(convidados), "convidados para o jantar.")

# 3.7 - Reduzindo a lista de convidados
print("Infelizmente só podemos convidar duas pessoas para o jantar.")
retirado = convidados.pop()
print(retirado, "você foi desconvidado.")
retirado = convidados.pop()
print(retirado, "você foi desconvidado.")
retirado = convidados.pop()
print(retirado, "você foi desconvidado.")
retirado = convidados.pop()
print(retirado, "você foi desconvidado.")
print(convidados[0], mensagem)
print(convidados[1], mensagem)
del convidados[0]
del convidados[0]
print(convidados)

# 3.8 - Conhecendo o mundo
cidades = ["barcelona", "londres", "nova iorque", "lisboa", "berlim"]
print(cidades)
print(sorted(cidades))
print(cidades)
print(sorted(cidades, reverse=True))
print(cidades)
cidades.reverse()
print(cidades)
cidades.reverse()
print(cidades)
cidades.sort()
print(cidades)
cidades.sort(reverse=True)
print(cidades)



