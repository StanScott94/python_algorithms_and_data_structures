class Node:

    def __init__(self, value):
        self.data = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.root == None:
            self.root = value
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value.data < current.data:
            if current.left_child == None:
                current.left_child = value
            else:
                self._insert(current.left_child, value)
        elif value.data > current.data:
            if current.right_child == None:
                current.right_child = value
            else:
                self._insert(current.right_child, value)

    def find_value(self, value):
        return self._find_value(self.root, value)

    def _find_value(self, current, value):
        if current:
            if value == current.data:
                return current.data
            elif value < current.data:
                return self._find_value(current.left_child, value)
            elif value > current.data:
                return self._find_value(current.right_child, value)

    def min_right_subtree(self, current):
        if current.left_child == None:
            return current
        else:
            return self.min_right_subtree(current.left_child)

    def delete_value(self, value):
        self._delete_value(None, self.root, None, value)

    def _delete_value(self, previous, current, is_left_node, value):
        if current:
            if value == current.data:
                if current.left_child and current.right_child:
                    min_child = self.min_right_subtree(current.right_child)
                    current.data = min_child.data
                    self._delete_value(current, current.right_child, False, min_child.data)
                elif current.left_child == None and current.right_child == None:
                    if previous:
                        if is_left_node:
                            previous.left_child = None
                        else:
                            previous.right_child = None
                    else:
                        self.root = None
                elif current.left_child == None:
                    if previous:
                        if is_left_node:
                            previous.left_child = current.right_child
                        else:
                            previous.right_child = current.right_child
                    else:
                        self.root = current.right_child
                else:
                    if previous:
                        if is_left_node:
                            previous.left_child = current.left_child
                        else:
                            previous.right_child = current.left_child
                    else:
                        self.root = current.left_child
            elif value < current.data:
                self._delete_value(current, current.left_child, True, value)
            elif value > current.data:
                self._delete_value(current, current.right_child, False, value)


    def in_order(self):
        self._in_order(self.root)
        print(" ")

    def _in_order(self, current):
        if current:
            self._in_order(current.left_child)
            print(current.data, end = " ")
            self._in_order(current.right_child)

    def pre_order(self):
        self._pre_order(self.root)
        print("")

    def _pre_order(self, current):
        if current:
            print(current.data, end = " ")
            self._in_order(current.left_child)
            self._in_order(current.right_child)

    def post_order(self):
        self._post_order(self.root)
        print("")

    def _post_order(self, current):
        if current:
            self._post_order(current.right_child)
            print(current.data, end = " ")
            self._post_order(current.left_child)
