class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class Stack:

    def __init__(self):
        self.stack_pointer = None

    def push(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.is_empty():
            self.stack_pointer = value
        else:
            value.next = self.stack_pointer
            self.stack_pointer = value

    def pop(self):
        if not self.is_empty():
            current_node = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            current_node.next = None
            return current_node.data

    def is_empty(self):
        return self.stack_pointer == None

    def peek(self):
        if not self.is_empty():
            return self.stack_pointer.data

    def __str__(self):
        string_value = ""
        current_node = self.stack_pointer
        while current_node is not None:
            string_value += str(current_node.data) + "->"
            current_node = current_node.next
        if string_value:
            return "[" + string_value[:-2]+ "]"
        return "[]"
