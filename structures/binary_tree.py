class Node:
    def __init__(self):
        self._p = None
        self._value = None
        self._left_p = None
        self._right_p = None

    @property
    def pointer(self):
        return self._p

    @property
    def value(self):
        return self._value

    @property
    def left_pointer(self):
        return self._left_p

    @property
    def right_pointer(self):
        return self._right_p

    @value.setter
    def value(self, value):
        self._value = value

    @left_pointer.setter
    def left_pointer(self, node):
        self._left_p = node

    @right_pointer.setter
    def right_pointer(self, node):
        self._right_p = node


class BinaryTree:
    def __init__(self):
        self.root = Node()

    def _insert_value(self, value: int, node: Node, part: str):
        new_node = Node()
        new_node.value = value
        if part == 'left':
            node.left_pointer = new_node
        else:
            node.right_pointer = new_node

    def _insert(self, value, node, is_root=False):
        if is_root:
            node.value = value
            return
        if node.left_pointer is not None and value < node.value:
            self._insert(value, node.left_pointer)
        elif node.left_pointer is None and value < node.value:
            self._insert_value(value, node, "left")
        elif node.right_pointer is not None and value >= node.value:
            self._insert(value, node.right_pointer)
        elif node.right_pointer is None and value >= node.value:
            self._insert_value(value, node, "right")

    def insert(self, value):
        if self.root.value is None:
            is_root = True
        else:
            is_root = False
        self._insert(value, self.root, is_root=is_root)

    def _show_values(self, node, depth, structure):
        if node.left_pointer is None and node.right_pointer is None:
            structure.setdefault(depth, []).append(node.value)
        if node.left_pointer is not None:
            self._show_values(node.left_pointer, depth+1, structure)
        if node.right_pointer is not None:
            self._show_values(node.right_pointer, depth + 1, structure)
        structure.setdefault(depth, []).append(node.value)

    def show_values(self):
        structure = {}
        self._show_values(self.root, depth=0, structure=structure)
        structure = sorted(
            [(k, v) for k, v in structure.items()], key=lambda x: x[0])
        return structure

