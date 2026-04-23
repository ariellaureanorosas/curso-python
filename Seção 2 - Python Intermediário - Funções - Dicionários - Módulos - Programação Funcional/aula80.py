# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# set_1 = {"Ariel", 1, 2, 3}
# print(set_1)
# --------------------------

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# import random

# numeros = [random.randint(1, 20) for _ in range(20)]

# lista = numeros.copy()
# set_1 = set(lista)
# for numero in set_1:
#     print(numero)
# --------------------------


# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add("Ariel")
s1.update("Olá Mundo")
s1.update(("Laureano", "Rosas"))
# s1.clear()
s1.discard("Laureano")
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2  # 1
s3 = s2 - s1  # 4
s3 = s2 ^ s1
print(s3)
