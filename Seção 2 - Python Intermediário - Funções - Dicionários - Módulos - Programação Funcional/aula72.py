# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


faixa = range(1, 11)

resultado = multiplicacao(*faixa)
print(resultado)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    return "impar"


print(par_impar(10))
