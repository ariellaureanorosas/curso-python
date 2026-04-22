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

    def limpar():
        os.system("cls" if os.name == "nt" else "clear")

    if opcao not in ("i", "a", "l", "s"):
        print("Digite a entrada corretamente")
        continue

    if opcao == "i":
        adiciona_item = input("Adicione o item: ".capitalize())
        limpar()
        lista_compras.append(adiciona_item.strip())

    elif opcao == "a":
        if not lista_compras:
            print(
                "Não tem como apagar, pois ainda não existe valores. Por favor insira um valor"
            )
            continue
        else:
            try:
                limpar()
                for indice, valor in enumerate(lista_compras):
                    print(f"[{indice}] - {valor}")
                print("-" * 30)
                apagar_item_lista = int(input("Digite o indice que quer apagar: "))
                item_removido = lista_compras.pop(apagar_item_lista)
                print(f"Removido - {item_removido}")
            except ValueError:
                print("Digite apenas números")
            except IndexError:
                print("o indice não existe na lista")
            except Exception:
                print("Erro desconhecido")

    elif opcao == "l":
        limpar()
        if not lista_compras:
            print("Não tem nenhum valor a ser exibido, por favor adicione a lista")
        else:
            for indice, valor in enumerate(lista_compras):
                print(f"[{indice}] - {valor}")
            print(f"A quantidade de itens é: [{len(lista_compras)}]")

    elif opcao == "s":
        print("Você decidiu Sair:")
        break
