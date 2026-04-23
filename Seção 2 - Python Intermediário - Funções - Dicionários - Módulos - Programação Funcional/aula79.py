# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]
# qtd_acertos = 0
# for pergunta in perguntas:
#     print(pergunta["Pergunta"])
#     print()  # pula uma linha

#     opcoes = pergunta["Opções"]
#     for indice, opcao in enumerate(opcoes):
#         print(f"{indice})", opcao)
#     print()  # pula uma linha

#     escolha = input("Digite uma opção: ")
#     escolha_int = None
#     acertou = False
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta["Resposta"]:
#                 acertou = True

#     if acertou:
#         print()  # pula uma linha
#         print("Acertou")
#         print()  # pula uma linha
#         qtd_acertos += 1
#     else:
#         print()  # pula uma linha
#         print("Errou")
#         print()  # pula uma linha

# print("QUANTIDADE DE ACERTOS:", qtd_acertos, "DE:", len(perguntas))
import os

qtd_acertos = 0

for pergunta in perguntas:
    while True:
        print(pergunta["Pergunta"])
        print()  # pula uma linha
        for i, opcao in enumerate(pergunta["Opções"]):
            print(f"{i})", opcao)
        print()  # pula uma linha
        entrada = input("Digite a alternativa correta: ")
        try:
            entrada_int = int(entrada)
            resposta = entrada_int
            opcoes = pergunta["Opções"]
            if resposta >= 0 and resposta < len(pergunta["Opções"]):
                if (
                    opcoes[resposta] == pergunta["Resposta"]
                ):  # -> mesma coisa de dizer: pergunta["Opções"][escolha_int]
                    print("Acertou")
                    print()  # pula uma linha
                    qtd_acertos += 1
                else:
                    print("Errou")
                    print()  # pula uma linha
                break
            else:
                print("Alternativa Inválida, por Favor digite novamente")
        except:
            os.system("cls" if os.name == "nt" else "clear")
            print("Entrada de dados inválida, digite corretamente por favor")
            print()  # pula uma linha

print("Quantidade de acertos", qtd_acertos)
