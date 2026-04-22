# Desempacotamento em chamadas de métodos e funções

string = "ABCD"
lista = ["Ariel", "Laureano", 1, 2, 3, "Rosas"]
tupla = "Python", "é", "Legal"
salas = [
    ["Ariel", "Rosas"],
    ["Luiz", "Ótavio"],
    ["João", "Eduarda", "Rebeca"],
]

primeiro, segundo, *_, penultimo, ultimo = lista

# print(primeiro, ultimo, penultimo)

# for nome in lista:
#     print(nome, end=" ")

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep="\n")
