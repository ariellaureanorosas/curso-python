# manipulando chaves e valores em dicionários

pessoa = {}

chave = "nome"
chave_2 = "sobrenome"

pessoa[chave] = "Ariel"
pessoa[chave] = "Laureano"  # altera o valor da chave
pessoa[chave_2] = "Rosas"
del pessoa[chave_2]  # apaga a chave do dicionário
print(pessoa)

if pessoa.get("sobrenome") is None:
    print("Não existe essa chave")
else:
    print(pessoa["sobrenome"])
