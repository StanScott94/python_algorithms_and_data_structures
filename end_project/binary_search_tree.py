from datetime import datetime, timedelta

class Node:

    def __init__(self, value):
        start_time, duration, job_title = value.split(",")
        start_time = datetime.strptime(start_time, '%H:%M:%S')
        formatted_start_time = start_time.time()
        formatted_end_time = (start_time + timedelta(minutes = int(duration))).time()

        self.start_time =formatted_start_time
        self.end_time = formatted_end_time
        self.duration = duration
        self.job_title = job_title.rstrip()
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Start Time: {self.start_time}, Duration: {self.duration}, Job Title: {self.job_title}"

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
        if value.start_time < current.start_time and value.end_time <= current.start_time:
            if current.left_child == None:
                current.left_child = value
                self._insert_result(value, True)
            else:
                self._insert(current.left_child, value)
        elif value.start_time > current.start_time and current.end_time <= value.start_time:
            if current.right_child == None:
                current.right_child = value
                self._insert_result(value, True)
            else:
                self._insert(current.right_child, value)
        else:
            self._insert_result(value, False)

    def _result(self, value):
        print(f"Job Title:\t\t {value.job_title}")
        print(f"Start Time:\t\t {value.start_time}")
        print(f"End Time:\t\t {value.end_time}")

    def _insert_result(self, value, wasInserted):
        print("=" * 70)
        if wasInserted:
            print(f"Inserted:")
            self._result(value)
        else:
            print(f"Rejected:")
            self._result(value)
        print("=" * 70)

    def _delete_value_result(self, value):
        print("=" * 70)
        print(f"Removed:")
        self._result(value)
        print("=" * 70)

    def find_value(self, value):
        return self._find_value(self.root, value)

    def _find_value(self, current, value):
        if current:
            if value == current.start_time:
                return current
            elif value < current.start_time:
                return self._find_value(current.left_child, value)
            elif value > current.start_time:
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
            if value == current.start_time:
                if current.left_child and current.right_child:
                    min_child = self.min_right_subtree(current.right_child)
                    current.start_time = min_child.start_time
                    self._delete_value(current, current.right_child, False, min_child.start_time)
                elif current.left_child == None and current.right_child == None:
                    if previous:
                        if is_left_node:
                            previous.left_child = None
                            self._delete_value_result(current)
                        else:
                            previous.right_child = None
                            self._delete_value_result(current)
                    else:
                        self.root = None
                        self._delete_value_result(current)
                elif current.left_child == None:
                    if previous:
                        if is_left_node:
                            previous.left_child = current.right_child
                            self._delete_value_result(current)
                        else:
                            previous.right_child = current.right_child
                            self._delete_value_result(current)
                    else:
                        self.root = current.right_child
                        self._delete_value_result(current)
                else:
                    if previous:
                        if is_left_node:
                            previous.left_child = current.left_child
                            self._delete_value_result(current)
                        else:
                            previous.right_child = current.left_child
                            self._delete_value_result(current)
                    else:
                        self.root = current.left_child
                        self._delete_value_result(current)
            elif value < current.start_time:
                self._delete_value(current, current.left_child, True, value)
            elif value > current.start_time:
                self._delete_value(current, current.right_child, False, value)

    def length(self):
        return self._length(self.root)

    def _length(self, current):
        if current is None:
            return 0
        return 1 + self._length(current.left_child) + self._length(current.right_child)

    def in_order(self):
        print("=" * 70)
        print("#\n# Jobs In Order \n#")
        print("=" * 70)
        self._in_order(self.root)
        print("=" * 70)

    def _in_order(self, current):
        if current:
            self._in_order(current.left_child)
            print(current)
            self._in_order(current.right_child)

    def pre_order(self):
        print("=" * 70)
        print("#\n# Jobs Pre Order \n#")
        print("=" * 70)
        self._pre_order(self.root)
        print("=" * 70)

    def _pre_order(self, current):
        if current:
            print(current, end = " ")
            self._in_order(current.left_child)
            self._in_order(current.right_child)

    def post_order(self):
        print("=" * 70)
        print("#\n# Jobs Post Order \n#")
        print("=" * 70)
        self._post_order(self.root)
        print("=" * 70)

    def _post_order(self, current):
        if current:
            self._post_order(current.right_child)
            print(current, end = " ")
            self._post_order(current.left_child)

    def _write_to_file(self, writer, current):
        if current:
            self._write_to_file(writer, current.left_child)
            writer.write(str(current.start_time) + "," + str(current.duration) + "," + current.job_title + "\n")
            self._write_to_file(writer, current.right_child)

    def write_to_file(self):
        custom_jobs_list = "custom_jobs.txt"
        with open(custom_jobs_list, "w") as writer:
            self._write_to_file(writer, self.root)
