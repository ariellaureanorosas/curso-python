# Try, except, else e finally

try:
    print("Abrir arquivo")

except ZeroDivisionError as error:
    print("Dividiu zero")
    print(error.__class__.__name__)
except IndexError as error:
    print(IndexError)
    print(error.__class__.__name__)
except (NameError, ImportError):
    print("nameError, Import Error")
else:
    print("Não deu Erro")
finally:  # sempre será executado
    print(2)
