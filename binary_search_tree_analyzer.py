import time
from data_types.binary_search_tree import BinarySearchTree

def generate_tree(size=None):
    b_s_t = BinarySearchTree()
    if size:
        #create large left and right scewed trees for analyzer
        pass
    else:
        b_s_t.insert("F")
        b_s_t.insert("T")
        b_s_t.insert("C")
        b_s_t.insert("S")
        b_s_t.insert("G")
        b_s_t.insert("W")
        b_s_t.insert("A")
        b_s_t.insert("X")
        b_s_t.insert("B")
        b_s_t.insert("O")
        b_s_t.insert("K")
        b_s_t.insert("H")
        b_s_t.insert("E")
        b_s_t.insert("N")
        b_s_t.insert("Q")
        b_s_t.insert("R")
        b_s_t.insert("V")
        b_s_t.insert("L")
        b_s_t.insert("Y")
        b_s_t.insert("D")
        b_s_t.insert("Z")
        b_s_t.insert("I")
        b_s_t.insert("P")
        b_s_t.insert("M")
        b_s_t.insert("J")
        b_s_t.insert("U")
    return b_s_t

def analyze_function(function_name, value):
    start_time = time.time()
    item = function_name(value)
    execution_time = time.time() - start_time
    print(f"{function_name.__name__.capitalize()} \t\t -> {value}, Time Elapsed : {execution_time:.20f}")

def binary_search_tree_analyzer():
    b_s_t = generate_tree()
    print("in order: ")
    b_s_t.in_order()
    print("pre order: ")
    b_s_t.pre_order()
    print("post order: ")
    b_s_t.post_order()
    analyze_function(b_s_t.find_value, "G")
    analyze_function(b_s_t.find_value, "W")
    analyze_function(b_s_t.delete_value, "K")
    analyze_function(b_s_t.delete_value, "F")
    analyze_function(b_s_t.delete_value, "z")

binary_search_tree_analyzer()
