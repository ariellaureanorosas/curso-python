import importlib
import aula100_modulo

print(aula100_modulo.variavel)

for i in range(10):
    importlib.reload(aula100_modulo)

print("fim")
