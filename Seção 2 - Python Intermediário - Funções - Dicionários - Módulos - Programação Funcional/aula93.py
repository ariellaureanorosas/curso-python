# Introdução ás Generator functions em Python
# generator = (n for n in range(10000))


# def generetor(number=0, maximium=10):
#     while True:
#         yield number
#         number += 1

#         if number >= maximium:
#             return


# gen = generetor(maximium=100)
# # print(next(gen))
# # print(next(gen))

# for n in gen:
#     print(n)


def generator(maximium=0):
    for number in range(0, maximium):
        if number % 2 == 0 and number % 5 == 0:
            yield f"{number} -> FizzBuzz"
        elif number % 3 == 0:
            yield f"{number} -> Fizz"
        elif number % 5 == 0:
            yield f"{number} -> Buzz"
        else:
            yield number


gen = generator(maximium=100)
for number in gen:
    print(number)
