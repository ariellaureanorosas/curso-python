"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


def calcular_a_e_b(a, b):
    resultado = a + b
    print(resultado)


def saudacao(nome="Sem nome"):
    print(f"Olá {nome}")


saudacao("Ariel")
