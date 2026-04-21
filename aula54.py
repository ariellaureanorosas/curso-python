"""
Tipo tupla - Uma lista imutável
"""

nomes = "Ariel", "Lauraeno", "Rosas"
nomes[1] = "outro"
_, _, nome, *resto = nomes  # não pode ser alterada
print(nomes)
print(nomes)
