numbers = [2, 5, 7, 0, 4, 45, 65, 37]


new_list = [num for num in numbers if num % 2 == 0]

print(new_list)


words = ['ecology', 'beta', 'foster', 'struct', 'automobile', 'boston', 'bddb']

word_list = [word.upper() if word.startswith('b') else word for word in words]
firs = map(str, word_list)

print(word_list, list(firs))