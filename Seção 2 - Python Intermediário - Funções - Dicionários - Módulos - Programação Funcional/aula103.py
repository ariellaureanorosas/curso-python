# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def cria_funcao(funcao, numero):
    def interna(operando):
        return funcao(operando, numero)

    return interna


soma_cinco = cria_funcao(soma, 10)
print(soma_cinco(10))
