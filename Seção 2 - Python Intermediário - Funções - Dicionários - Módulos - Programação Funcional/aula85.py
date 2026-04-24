# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# (a, a2), (b, b2) = pessoa.items()
# print(a, a2)
# print(b, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

dados_pessoa = {"idade": 16, "altura": 1.6}

pessoa_completa = {**pessoa, **dados_pessoa}
# mesma coisa que:
pessoa_completa = pessoa.copy()
pessoa_completa.update(dados_pessoa)
# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados_e_nao_nomeados(*args, **kwargs):
    print("argumentos não nomeados:", args)
    print("argumentos nomeados:", kwargs)


mostro_argumentos_nomeados_e_nao_nomeados(1, 2, 3, 4, nome="Ariel", idade=18)

configuracoes = {"arg1": 1, "arg2": 2, "arg3": 3, "arg4": 4, "arg5": 5}

mostro_argumentos_nomeados_e_nao_nomeados(**configuracoes)
mostro_argumentos_nomeados_e_nao_nomeados(configuracoes)
