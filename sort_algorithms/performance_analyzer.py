from random import randint
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort_inplace import quick_sort_inplace
from quick_sort_basic import quick_sort_basic
from heap_sort import heap_sort

def user_input():
    list_size = int(input("define list size to analyze: "))
    maximun_value_of_list = int(input("define maximunpossible value of the list: "))
    iterations = int(input("define number of iterations of performance analyzer: "))
    print(f"\nlist of {list_size} items, with maximun possible value of {maximun_value_of_list}, running {iterations} times")
    print(f"depending on list size some algorithms might not be displayed\n")
    print("=" * 60)
    return list_size, maximun_value_of_list, iterations

def list_generator(list_size, maximun_value):
    return [randint(0, maximun_value) for value in range(list_size)]

def analyze_function(function_name, *arguments):
    start_time = time.time()
    function_name(*arguments)
    execution_time = time.time() - start_time
    print(f"{function_name.__name__.capitalize()} \t\t -> Time Elapsed: {execution_time:.5f}")

def performance_analyzer():
    running = True
    while running:
        try:
            list_size, maximun_value_of_list, iterations = user_input()
            list_to_sort = list_generator(list_size, maximun_value_of_list)

            for iteration in range(iterations):
                if list_size <= 10000:
                    analyze_function(bubble_sort, list_to_sort.copy())
                    analyze_function(insertion_sort, list_to_sort.copy())
                if list_size <= 15000:
                    analyze_function(selection_sort, list_to_sort.copy())
                if list_size <= 1000000:
                    analyze_function(quick_sort_inplace, list_to_sort.copy())
                if list_size <= 1500000:
                    analyze_function(merge_sort, list_to_sort.copy())
                if list_size <= 3000000:
                    analyze_function(quick_sort_basic, list_to_sort.copy())
                if list_size <= 10000000:
                    analyze_function(heap_sort, list_to_sort.copy())
                    analyze_function(sorted, list_to_sort.copy())
                print("=" * 60)
        except ValueError:
            print("invalid input\n")
        except KeyboardInterrupt:
            print("\nGoodbye")
            running = False

performance_analyzer()
