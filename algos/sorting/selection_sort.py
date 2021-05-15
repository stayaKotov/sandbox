import typing as t
import copy


class SelectionSort:
    def __init__(self, elements: t.List):
        self.elements = elements

    def sort(self):
        res_elems = copy.deepcopy(self.elements)
        n = len(res_elems)
        i = 0
        for i, key_elem in enumerate(res_elems[:-1]):
            min_elem, min_ix = None, None
            for j in range(i+1, n):
                cur_elem = res_elems[j]
                if min_elem is None or cur_elem < min_elem:
                    min_elem = cur_elem
                    min_ix = j
            if min_elem < key_elem:
                res_elems[i], res_elems[min_ix] = res_elems[min_ix], res_elems[i]
            i += 1
        return res_elems
