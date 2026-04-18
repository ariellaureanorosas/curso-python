"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input("Digite o número que você quer dobrar: ")

try:
    print(numero_str)
    numero_float = float(numero_str)
    print(f"O dobro de {numero_str} é {numero_float}")
except:
    print("Isso não é um número")
