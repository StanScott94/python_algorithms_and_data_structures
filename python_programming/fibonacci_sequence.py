def recursive_fibonacci_calculator(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return recursive_fibonacci_calculator(n - 1) + recursive_fibonacci_calculator(n - 2)

def fibonacci_sequence(n):
    print(f"The {n}th numer of the fibonnaci sequence is {recursive_fibonacci_calculator(n)}")

number_to_calculate = 0
fibonacci_sequence(number_to_calculate)
number_to_calculate = 1
fibonacci_sequence(number_to_calculate)
number_to_calculate = 10
fibonacci_sequence(number_to_calculate)
number_to_calculate = 20
fibonacci_sequence(number_to_calculate)
