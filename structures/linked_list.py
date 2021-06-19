class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class BiNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None


class LinkedList:
    def __init__(self):
        self.iterator = None
        self.root = None

    def get_iterator(self):
        """complexity O(1)"""
        return self.iterator

    def add(self, value):
        """complexity O(1)"""
        new_node = Node(value)
        if self.root is None:
            self.root = Node(0)
            self.iterator = self.root
            self.iterator.value = new_node.value
        else:
            self.iterator.next = new_node
            self.iterator = self.iterator.next

    def remove(self, value):
        """Complexity O(n)"""
        it = self.root
        prev_el = None
        while True:
            if it is None:
                return False
            if it.value == value:
                if prev_el is None:
                    self.root = it.next
                else:
                    prev_el.next = it.next
                return True
            prev_el = it
            it = it.next

    def contains(self, value):
        """Complexity O(n)"""
        it = self.root
        while True:
            if it is not None:
                if it.value == value:
                    return True
                it = it.next
            else:
                return False

    def count(self):
        """Complexity O(n)"""
        it = self.root
        s = 0
        while True:
            if it is not None:
                s += 1
            else:
                return s
            it = it.next

    def print(self):
        it = self.root
        while it.next is not None:
            print(f"value = {it.value}")
            it = it.next
        if it.next is None and it.value is not None:
            print(f"value = {it.value}")


class BiLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def get_iterator(self):
        """complexity O(1)"""
        return self.iterator

    def add_last(self, value):
        """complexity O(1)"""
        new_node = Node(value)
        if self.root is None:
            self.root = Node(0)
            self.iterator = self.root
            self.iterator.value = new_node.value
            self.tail = self.root
        else:
            new_node.prev = self.iterator
            self.iterator.next = new_node
            self.iterator = self.iterator.next
            self.tail = self.iterator

    def add_first(self, value):
        """complexity O(1)"""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.tail = self.root
        else:
            tmp_node = self.root
            self.root = new_node
            self.root.next = tmp_node
            tmp_node.prev = self.root

    def remove_last(self):
        """Complexity O(1)"""
        self.tail = self.tail.prev

    def contains(self, value):
        """Complexity O(n)"""
        it = self.root
        while True:
            if it is not None:
                if it.value == value:
                    return True
                it = it.next
            else:
                return False

    def count(self):
        """Complexity O(n)"""
        it = self.root
        s = 0
        while True:
            if it is not None:
                s += 1
            else:
                return s
            it = it.next

    def print(self):
        it = self.root
        while it.next is not None:
            print(f"value = {it.value}")
            it = it.next
        if it.next is None and it.value is not None:
            print(f"value = {it.value}")
