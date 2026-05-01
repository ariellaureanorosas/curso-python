# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


def nao_aceito_zero(divisor):
    if divisor == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True


def int_ou_float(number):
    tipo = type(number)
    if not isinstance(number, (int, float)):
        raise TypeError(
            f"'{number}' deve ser int ou float" f"'{tipo.__name__}' enviado"
        )
    return True


def divide(number, divisor):
    int_ou_float(number)
    int_ou_float(divisor)
    nao_aceito_zero(divisor)
    return number / divisor


print(divide(8, 0))
