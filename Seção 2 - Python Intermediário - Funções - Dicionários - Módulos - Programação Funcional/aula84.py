def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


print(executa(lambda x, y: x + y, 2, 3))  # função redefinida com lambda

# --------------------------------------------------------------------


def cria_multiplicado(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


duplica = executa(lambda m: lambda n: n * m, 2)  # função redefinida com lambda

print(duplica(2))

produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900},
]

lista_ordenada = sorted(produtos, key=lambda item: item["preco"], reverse=True)

for item in lista_ordenada:
    print(item)

soma = lambda *args: sum(args)
print(soma(1, 2, 3, 4, 5, 6, 7))

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))
