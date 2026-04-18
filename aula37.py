"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

limite = int(input("Digite um limite: "))
contador = 0
passo = int(input("Digite uma incrementação: "))

while contador <= limite:
    contador += passo

    if contador == 10:
        print("não vou mostrar o 10")
        continue

    if 20 <= contador <= 30:
        print("não vou mostrar os valores")
        continue

    print(contador)

print("Acabou")
