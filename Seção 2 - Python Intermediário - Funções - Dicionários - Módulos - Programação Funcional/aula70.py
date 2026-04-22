"""
Retorno de valores das funções (return)
"""

# varialvel = print("Ariel")
# print(
#     varialvel
# )  # retornou um valor none porque a função print não retorna valor nenhum


def soma(a, b):
    if a > 10:
        return [10, 20]
    return a + b


soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma1)
print(soma2)
print(soma(11, 50))
