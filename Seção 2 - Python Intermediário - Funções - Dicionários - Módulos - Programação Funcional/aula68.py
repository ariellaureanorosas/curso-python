"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def soma(a, b, c=None):
    if c is not None:
        print(f"{a=} {b=} {c=}", a + b + c)
    else:
        print(f"{a=} {b=}", a + b)


soma(1, 2)
soma(1, 2, 3)
