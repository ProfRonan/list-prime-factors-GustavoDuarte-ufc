"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    b = number
    for i in range(2, b+1):
        if b % i == 0:
            b += 1
    if b != 1:
        return False
    else:
        return True


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    c = number
    d = 2
    lista = []
    while d < c+1:
        if c % d == 0:
            lista.append(d)
            c = c/d
            d = 2
        else:
            d+=1
    return lista