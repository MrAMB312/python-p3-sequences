#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    if length == 0:
        print([])
    elif length > 0:
        print(fibonacci_list[0:length])
    else:
        print("Error: cannot take negative value as argument")