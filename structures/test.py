import numpy as np
from binary_tree import BinaryTree
from linked_list import LinkedList, BiLinkedList


def test_btree():
    ar = list(map(int, np.random.randint(-10, 10, 10)))
    print(ar)
    # ar = [1, 2, 3, 4, 5, 6, 7, 8]
    bt = BinaryTree()
    for el in ar:
        bt.insert(el)
    print(bt.show_values())


def test_lk():
    ar = list(map(int, np.random.randint(-10, 10, 10)))
    print(ar)
    lk = LinkedList()
    for el in ar:
        lk.add(el)
    lk.print()


def test_blk():
    ar = list(map(int, np.random.randint(-10, 10, 10)))
    print(ar)
    lk = BiLinkedList()
    for el in ar:
        lk.add_last(el)
    lk.print()


if __name__ == "__main__":
    # test_btree()
    test_blk()
