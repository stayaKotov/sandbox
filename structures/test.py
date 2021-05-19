import numpy as np
from binary_tree import BinaryTree


def test_btree():
    ar = list(map(int, np.random.randint(-10, 10, 10)))
    print(ar)
    # ar = [1, 2, 3, 4, 5, 6, 7, 8]
    bt = BinaryTree()
    for el in ar:
        bt.insert(el)
    print(bt.show_values())


if __name__ == "__main__":
    test_btree()
