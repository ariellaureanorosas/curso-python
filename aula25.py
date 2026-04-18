# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X- Hexadecimal (ABCDEF0123456789)

nome = "Ariel"
preco = 1000.12398712
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %08X" % (15123, 15123))
