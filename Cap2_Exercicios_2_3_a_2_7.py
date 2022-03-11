# Exercício 2.3 - Mensagem pessoal
nome = "Eric"
print("Alô", nome, ", você gostaria de aprender um pouco de Python hoje?")

# Exrcicio 2.4 - Letras Maiúsculas e Minúsculas em nomes
nome = "anDré luiZ fiGueiredo raFful"
print(nome)
print(nome.lower())
print(nome.upper())
print(nome.title())

# Exercício 2.5 - Citação famosa
print('André Rafful uma vez disse: "Se minha avó tivesse 6 rodas ela seria um ônibus".')

# Exercício 2.6 - Citação famosa com variáveis
pessoa_famosa_eu = "André Rafful"
mensagem = pessoa_famosa_eu + ' uma vez disse: "Se minha avó tivesse 6 rodas ela seria um ônibus".'
print(mensagem)

# Exercício 2.7 - Removendo caracteres em branco dos nomes
espacos_a_direita = "espaço a direita\t"
espacos_a_esquerda = "\tespaço a esquerda"
espacos_nos_dois_lados = "\nespaços dos dois lados \t"
print("\n==< SEM FORMATAÇÃO >==")
print(espacos_a_esquerda, espacos_nos_dois_lados, espacos_a_direita)
print("\n==< FORMATADO >==")
print(espacos_a_esquerda.lstrip(), espacos_nos_dois_lados.strip(), espacos_a_direita.rstrip())




