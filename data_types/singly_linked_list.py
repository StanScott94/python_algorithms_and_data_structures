class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_value(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head = value
        else:
            self.tail.next = value
        self.tail = value

    def prepend_value(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head = value
            self.tail = value
        else:
            value.next = self.head
            self.head = value

    def find_value_index(self, value):
        index = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                return index
            else:
                current_node = current_node.next
                index += 1

    def remove_value_at_index(self, index_to_remove):
        current_node = self.head
        previous_node = None
        for node in range(index_to_remove+1):
            if node == index_to_remove and current_node is not None:
                previous_node.next = current_node.next
            elif current_node is not None:
                    previous_node = current_node
                    current_node = current_node.next

    def length(self):
        index = 0
        current_node = self.head
        while current_node is not None:
            index += 1
            current_node = current_node.next
        return index

    def revese_list(self, current):
        if current == None or current.next == None:
            self.tail = self.head
            self.head = current
            return current
        head = self.revese_list(current.next)
        current.next.next = current
        current.next = None
        return head

    def __str__(self):
        string_value = ""
        current_node = self.head
        while current_node is not None:
            string_value += str(current_node.data) + "->"
            current_node = current_node.next
        if string_value:
            return "[" + string_value[:-2]+ "]"
        return "[]"
