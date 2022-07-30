import time
# def decorator(function):
#     def wrapper(*args ,**kwargs):
#         print('I just understood decorators')
#         return function(*args, **kwargs)

#     return wrapper


# @decorator
# def hello_world(person):
#     return (f'Morbius {person}')

# print(hello_world("lupita"))

# #print(fun)

# Logging decorator

# def logged(function):
#     def wrapper(*args ,**kwargs):
#         # assigning your variables is recommended
#         value = function(*args, **kwargs)
#         with open('info.txt', 'a+') as f:
#             fname = function.__name__
#             f.write(f'{fname} returned value {value}')
#             print(f.write(f'{fname} returned value {value}\n'))
#             return value
#     return wrapper


# @logged
# def added( x, y):
#     return x + y

# print(added(2,5))

# function time benchmarking decorator

# A decorator to test the spped of execution of a function


def timer(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} executed in {after-before} seconds')
        return value

    return wrapper

@timer
def runner(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

print(runner(1000000))