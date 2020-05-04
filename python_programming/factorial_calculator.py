def recursive_factorial_calculator(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial_calculator(n - 1)

number_to_calculate = 0 # expecting 1
print(f"The factorial of {number_to_calculate} is {recursive_factorial_calculator(number_to_calculate)}")
number_to_calculate = 1 # expecting 1
print(f"The factorial of {number_to_calculate} is {recursive_factorial_calculator(number_to_calculate)}")
number_to_calculate = 5 # expecting 120
print(f"The factorial of {number_to_calculate} is {recursive_factorial_calculator(number_to_calculate)}")
