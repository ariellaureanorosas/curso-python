# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

pessoa = {"nome": "Ariel", "sobrenome": "Rosas"}
d1 = {"c1": 1, "c2": 2, "l1": [1, 2, 3]}


# print(len(pessoa))
# print(pessoa.keys()) -> eu posso converter para uma lista ou tupla: print(list(pessoa.keys()))
# print(pessoa.values()) -> eu posso converter para uma lista ou tupla: print(list(pessoa.values()))
# print(pessoa.items()) -> eu posso converter para uma lista ou tupla: print(list(pessoa.items()))
# pessoa.setdefault("idade", None)
# print(pessoa["idade"])
# d2 = d1.copy() -> shallow copy (cópia rasa)
# d2 = copy.deepcopycopy(d1) -> deep copy (cópia profunda)
# print(pessoa.get("idade", None))
# nome = pessoa.pop("nome")
# ultima_chave = pessoa.popitem()
pessoa.update({"nome": "novo valor", "idade": 18})

pessoa.update(sobrenome="Laureano", peso=55)
tupla = (("chave_tupla", "valor"), ("chave_tupla_2", "valor_chave_tupla_2"))
pessoa.update(tupla)
lista = [["chave_lista", "valor"], ["chave_lista_2", "valor_chave_lista_2"]]
pessoa.update(lista)

for chave, valor in pessoa.items():
    print(chave, valor)

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
