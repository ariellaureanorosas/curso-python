for indice in range(10):
    if indice == 2:
        print("índice é 2, Pulando...")
        continue

    if indice == 8:
        print("índice é 8, seu else não executará")
        break

    for j in range(1, 3):
        print(indice, j)
        print(indice, j)
else:
    print("For Completo com Sucesso!")
