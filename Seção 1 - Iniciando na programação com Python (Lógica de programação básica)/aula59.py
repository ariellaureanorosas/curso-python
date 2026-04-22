"""
Lista de listas e seus indices
"""

salas = [
    ["Ariel", "Rosas"],
    ["Luiz", "Ótavio"],
    ["João", "Eduarda", "Rebeca"],
]

# print(salas[2][3][2])

for sala in salas:
    for aluno in sala:
        print(aluno)
