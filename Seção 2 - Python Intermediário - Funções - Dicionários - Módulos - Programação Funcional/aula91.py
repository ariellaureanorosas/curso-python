# dir, hasattr e getattr em python

string = "Ariel"
metodo = "upper"


if hasattr(string, metodo):
    print("existe upper")
    print(getattr(string, metodo)())
else:
    print("não existe o método", metodo)
