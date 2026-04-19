"""Calculadora com while"""

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    # ------------------CHECAGEM DOS NÚMEROS------------------#
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    # --------------CHECAGEM DE OPERADORES-------------------#
    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    # --------------------OPERAÇÃO--------------------------#
    if operador == "+":
        print(
            f"O resultado entre {numero_1} e {numero_2} é {num_1_float + num_2_float}"
        )
    elif operador == "-":
        print(
            f"O resultado entre {numero_1} e {numero_2} é {num_1_float - num_2_float}"
        )
    elif operador == "*":
        print(
            f"O resultado entre {numero_1} e {numero_2} é {num_1_float * num_2_float}"
        )
    elif operador == "/":
        print(
            f"O resultado entre {numero_1} e {numero_2} é {num_1_float / num_2_float}"
        )

    # -------------------CHECAGEM DE SAÍDA---------------------------#
    saida = input("Você quer sair: [S] ou [N] ").strip().lower()
    checagem_saida = saida == "s" or saida.__contains__("sim")

    if checagem_saida == True:
        print("Você decidiu Sair!")
        break
