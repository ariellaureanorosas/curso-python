"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# lembre-te do desempacotamento
x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


numeros = range(1, 11)
print(soma(*numeros))
print(sum(numeros))
