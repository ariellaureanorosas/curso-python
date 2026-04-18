"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# EXERCÍCIO 1:

# numero_inteiro = input('Insira um número: ')
# try:
#     numero_formatado = int(numero_inteiro)
#     if numero_formatado % 2 == 0:
#             print('Esse número é par')
#     else:
#         print('número impar')
# except:
#     print('Número digitado incorretamente')


# EXERCÍCIO 2:

# hora = input('Que horas são: ')

# try:
#      hora_formatada = float(hora)
#      if hora_formatada >= 0 and hora_formatada <= 11:
#           print('Bom dia')
#      elif hora_formatada >= 12 and hora_formatada <= 17:
#           print('Boa tarde!')
#      elif hora_formatada >= 18 and hora_formatada <= 23:
#           print('Boa noite!')
#      else: print('Digite uma hora válida')
# except:
#      print('Insira uma hora válida!')

# EXERCÍCIO 3:

nome_usuario = input("Insira seu nome: ")
try:
    if len(nome_usuario) <= 4:
        print("Seu nome è muito curto")
    elif 5 <= len(nome_usuario) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
except:
    print("Digite um nome corretamente")
