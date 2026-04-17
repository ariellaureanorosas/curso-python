# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  A r i e l
# -5-4-3-2-1

# nome = 'Ariel'
# print(nome[2])
# print(nome[-2])
# print('w' in nome)
# print('w' not in nome)

nome = input('Insira seu nome: ')
encontrar = input('digite o que você quer procurar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')