"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"

    return saudar


saudacao_bom_dia = criar_saudacao("Bom dia")
saudacao_boa_noite = criar_saudacao("Boa noite")

for nome in ["Ariel", "Laureano", "Rosas"]:
    print(saudacao_bom_dia(nome))
    print(saudacao_boa_noite(nome))
