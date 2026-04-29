import sys

# Generator expression, iterables e iterators em python
iterable = ["eu", "tenho", "__iter__"]
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generetor = (number for number in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generetor))
