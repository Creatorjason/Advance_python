import sys

def generator(n):
    for x in range(1, n):
        yield x ** 3


value = generator(1200000000000)
print(sys.getsizeof(value))



def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 3

value = infinite_sequence()

print(next(value))
print(next(value))
print(next(value))
print(next(value))