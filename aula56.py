"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista_compras = []

while True:

    print("-" * 30)
    opcao = input("Selecione uma opção:\n[I]nserir [A]pagar [L]istar [S]air: ").lower()
    print("-" * 30)

    if opcao not in ("i", "a", "l", "s"):
        print("Digite a entrada corretamente")

    if opcao == "i":
        adiciona_item = input("Adicione o item: ".capitalize())
        os.system("cls" if os.name == "nt" else "clear")
        lista_compras.append(adiciona_item.strip())

    elif opcao == "a":
        if len(lista_compras) == 0:
            print(
                "Não tem como apagar, pois ainda não existe valores. Por favor insira um valor"
            )
        else:
            try:
                os.system("cls" if os.name == "nt" else "clear")
                for indice, valor in enumerate(lista_compras):
                    print(f"[{indice}] - {valor}")
                print("-" * 30)
                apagar_item_lista = int(input("Digite o indice que quer apagar: "))
                lista_compras.pop(apagar_item_lista)
            except ValueError:
                print("Digite apenas números")
            except IndexError:
                print("o indice não existe na lista")
            except Exception:
                print("Erro desconhecido")

    elif opcao == "l":
        os.system("cls" if os.name == "nt" else "clear")
        if len(lista_compras) == 0:
            print("Não tem nenhum valor a ser exibido, por favor adicione a lista")
        else:
            for indice, valor in enumerate(lista_compras):
                print(f"[{indice}] - {valor}")
            print(f"A quantidade de itens é: [{len(lista_compras)}]")

    elif opcao == "s":
        print("Você decidiu Sair:")
        break
