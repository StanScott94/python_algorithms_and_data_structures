import random

# Question 1: Use list comprehension to update the code below and
# assign my_list to be a list of 200 random integers ranging in values
# between 25 and 500. Hint: Use the randint function
my_list = [random.randint(25,500) for num in range(200)]

# Question 2 (4 parts): Cast my_list to a set and re-assign to my_list as a list.
# Go through the steps below and see if you can find out how many duplicate
# values were removed.
initial_size = len(my_list)
print(f"Initial size of my_list: {initial_size}")
# cast the list to a set to remove duplicates and re-assign to my_list as a list
my_list = list(set(my_list))
final_size = len(my_list)
print(f"Final size of my_list after removing duplicates: {final_size}")
dups_removed = initial_size - final_size
print(f"Number of integers removed: {dups_removed}")
print('-'*40)
print()

# Question 3: What is the largest integer in my_list?
largest_val = max(my_list)
print(f"Largest integer in my_list: {largest_val}")
print('-'*40)
print()

# Question 4: What is the smallest value in my_list?
smallest_val = min(my_list)
print(f"Smallest integer in my_list: {smallest_val}")
print('-'*40)
print()

# Question 5: Create a tuple with the exact same values as my_list
# name it my_tuple
my_tuple = tuple(my_list)

# Question 6: What are the last 3 values of my_tuple?
my_tuple_last_val = my_tuple[-1]
my_tuple_sec_last_val = my_tuple[-2]
my_tuple_third_last_val = my_tuple[-3]
print(f"The last 3 values of the tuple are {(my_tuple_third_last_val,my_tuple_sec_last_val,my_tuple_last_val)}")
print('-'*40)
print()

# Question 7: Create a new tuple with all the values of my_tuple in
# reversed order
my_new_tuple = my_tuple[::-1]

# Question 8: Does the first integer of my_new_tuple match my_tuple_last_val?
# Enter in the conditional below that will evaluate to True or False
comparison = my_new_tuple[0] == my_tuple_last_val
print(f"First integer of my_new_tuple matches last integer of my_tuple is a {comparison} statement")
print('-'*40)
print()

# Question 9: Create a new tuple with the first 5 integers of my_new_tuple
my_other_tuple = my_new_tuple[:5]
print(f"My newly created 5 integer tuple is {my_other_tuple}")
print('-'*40)
print()

# Question 10: Do the integer values (ignore order) of my_other_tuple match the values of
# the last 5 integers in my_list? Replace the boolean below with
# a conditional that evaluates to True or False.
tuple_and_list_comp = sorted(my_other_tuple) == my_list[len(my_list)-5:]
print(f"Integers in my_other_tuple match the last 5 integers of my_list is a {tuple_and_list_comp} statement")
print('-'*40)
print()

# Question 11: Find the intersection between the following two sets and
# store it in my_match, ignore format
my_requirements = {'ruby','python'}
available_languages = {"comp sci", "physics", "elec engr", "philosophy", "python"}
my_match = my_requirements.intersection(available_languages)
print(f"I can take {my_match} since I need it and it's available")
print('-'*40)
print()

# (Challenge) Question 12: Given the dictionary below, create a list called my_al_list
# which includes only the values (meaning) associated with each word.
# my_al_list should look like ['the round fruit of a tree of the rose family',
# 'an insect which cleans up the floor'......].
# Obviously do this programmatically and don't hardcode it, you may use
# other lines of code and variables as you see fit. Solution code has a couple of
# options displayed.

word_dict = {'a':
                {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor'
                },
             'b':
                {
                 'bad': 'of poor quaity or low standard',
                 'business': 'season 8 of GOT'
                }
            }

# Option 1, simple nested for loop and append combo
my_al_list = []
for letter, combo in word_dict.items():
    for meaning in combo.values():
        my_al_list.append(meaning)
print(f"The meanings in the dictionary are {my_al_list}")

# Option 2, list comprehension
my_al_list = [list(combo.values()) for index, combo in word_dict.items()]
# Flatten to remove list of lists and convert to a single list
my_al_list = [meaning for meanings in my_al_list for meaning in meanings]
print(f"The meanings in the dictionary are {my_al_list}")

# Option 3 (advanced), use itertools chain + list comprehension combo
from itertools import chain
my_al_list = list(chain.from_iterable([list(combo.values()) for index, combo in word_dict.items()]))
print(f"The meanings in the dictionary are {my_al_list}")
