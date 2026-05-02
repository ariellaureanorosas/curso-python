from sys import path

import aula101_package.modulo

# from aula101_package.modulo import soma_do_modulo
from aula101_package import modulo
from aula101_package.modulo import *

print(soma_do_modulo(1, 2))
print(aula101_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
