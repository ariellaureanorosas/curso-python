# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.


def cria_multicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


multiplo_de_dois = cria_multicador(2)
multiplo_de_tres = cria_multicador(3)
multiplo_de_quatro = cria_multicador(4)

print(multiplo_de_dois(10))
print(multiplo_de_tres(10))
print(multiplo_de_quatro(10))
