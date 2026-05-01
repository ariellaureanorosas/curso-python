# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import aula99_modulo
from aula99_modulo import soma, variavel_modulo

# print("Este módulo se chama", __name__)
print(aula99_modulo.variavel_modulo)
print(aula99_modulo.soma(5, 5))
print(variavel_modulo)
print(soma(10, 20))
