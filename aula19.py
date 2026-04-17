primeiro_valor = input('Digite um valor: ')
segundo_valor = input('digite outro valor: ')

if primeiro_valor == segundo_valor:
    print('os valores são iguais')
elif primeiro_valor > segundo_valor:
    print(f'o primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}')
else:
    print(f'o segundo valor: {segundo_valor} é maior que o primeiro valor: {primeiro_valor}')