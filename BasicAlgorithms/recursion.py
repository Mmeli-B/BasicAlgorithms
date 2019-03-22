def sum_array(array):
    sum = 0
    if len(array) < 1: return sum 
    else: 
        sum += array.pop(0)
        return sum_array(array)

def fibonacci(n):
    if n <= 1: return n
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n <= 1: return n
    else: return n * factorial(n - 1)

def reverse(word):
    reversed_word = ''
    for char in reversed(word): reversed_word += char
    return reversed_word