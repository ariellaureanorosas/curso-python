"""
Introdução ao desempacotamento + tuples (tuplas)
"""

# nomes = ["Ariel", "Lauraeno", "Rosas"]
# nome1, nome2, nome3 = nomes
# print(nome2)


_, nome2, *_ = ["Ariel", "Lauraeno", "Rosas"]
print(nome2)  # Lauraeno
