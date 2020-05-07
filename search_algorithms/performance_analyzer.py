import time
from random import randint, choice
from string import ascii_lowercase as letters
from linear_search import linear_search
from binary_search import binary_search

def user_input():
    print(f"list size capped at 2,000,000 for performace reasons")
    list_size = int(input("define list size to analyze: "))
    iterations = int(input("define number of iterations of performance analyzer: "))
    print(f"\nlist of {list_size} items, running {iterations} times")
    print("=" * 60)
    return list_size, iterations

def generate_name(length_of_name):
        return ''.join(choice(letters) for index in range(length_of_name))

def list_generator(list_size, length_of_name, list_of_domains, email_to_find):
    list_of_emails = []
    for index in range(list_size):
        list_of_emails.append(generate_name(length_of_name) + choice(list_of_domains))

    list_of_emails.append(email_to_find)
    return sorted(list_of_emails)

def analyze_function(function_name,*arguments):
    start_time = time.time()
    item_found, index = function_name(*arguments)
    execution_time = time.time() - start_time
    print(f"{function_name.__name__.capitalize()} \t\t -> found {item_found}, at index {index} Time Elapsed : {execution_time:.5f}")

def performance_analyzer():
    running = True
    while running:
        try:
            list_size, iterations = user_input()
            if list_size <= 2000000:
                list_of_domains = ["@python.com", "@java.co.uk", "@cobol.net", "@assembler.co.za"]
                email_to_find = "you_found_me@nice.com"
                length_of_name = 10

                for iteration in range(iterations):
                    list_to_search = list_generator(list_size, length_of_name, list_of_domains, email_to_find)
                    analyze_function(linear_search, email_to_find, list_to_search)
                    analyze_function(binary_search, email_to_find, list_to_search)
                    print("=" * 60)
        except ValueError:
            print("invalid input\n")
        except KeyboardInterrupt:
            print("\nGoodbye")
            running = False

performance_analyzer()
