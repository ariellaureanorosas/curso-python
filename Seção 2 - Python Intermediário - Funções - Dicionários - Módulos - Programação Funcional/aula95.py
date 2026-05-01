# Try, except, else e finally
try:
    a = 18
    # b = 0
    # c = a / b
    print("linha 1"[10000])
except ZeroDivisionError as error:
    print("Dividiu por zero")
    print(error)
except NameError:
    print("Nome B não está definido")
except (TypeError, IndexError) as error:
    print("TypeError + IndexERRor")
    print(error)
    print(error.__class__.__name__)
except Exception:
    print("Erro Desconhecido")
