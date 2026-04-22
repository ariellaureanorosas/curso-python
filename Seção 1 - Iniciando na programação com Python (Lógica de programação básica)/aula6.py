# conversão de tipos, coerção
# Type convertion, typecasting, coercion é o ato de converter um tipo em outro
# Tipos imutáveis e primitivos: str, int, float, bool

print(1 + 1)
print("a" + "b")
# print('a' + 1) -> dá erro

print(int("1"), type(int("1")))
print(int("1") + 1)
print(float("1") + 1)
print(bool(" "))  # sem espaço dá falso com espaço dá True
