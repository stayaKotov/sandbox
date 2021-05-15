from bubble_sort import BubbleSort
from insert_sort import InsertSort
from selection_sort import SelectionSort
from merge_sort import MergeSort
import numpy as np


def run_bubble_sort():
    ll = np.random.randint(-10, 10, 10)#[7, 6, 5, 4, 3, 2, 1]
    bs = BubbleSort(ll)
    res = bs.sort()
    print("BubbleSort")
    print(f"before: {ll}")
    print(f"after: {res}")
    print()


def run_selection_sort():
    ll = np.random.randint(-10, 10, 10)#[7, 6, 5, 4, 3, 2, 1]
    ss = SelectionSort(ll)
    res = ss.sort()
    print("SelectionSort")
    print(f"before: {ll}")
    print(f"after: {res}")
    print()


def run_insert_sort():
    ll = np.random.randint(-10, 10, 10)#[7, 6, 5, 4, 3, 2, 1]
    _is = InsertSort(ll)
    res = _is.sort()
    print("InsertSort")
    print(f"before: {ll}")
    print(f"after: {res}")
    print()


def run_merge_sort():
    ll = np.random.randint(-10, 10, 10)#[7, 6, 5, 4, 3, 2, 1]
    print(ll)
    _is = MergeSort(ll)
    res = _is.sort()
    print("MergeSort")
    print
    print(f"before: {ll}")
    print(f"after: {res}")
    print()


if __name__ == "__main__":
    # run_bubble_sort()
    # run_selection_sort()
    # run_insert_sort()
    run_merge_sort()
