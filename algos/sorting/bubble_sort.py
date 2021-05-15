import typing as t
import copy


class BubbleSort:
    def __init__(self, elements: t.List):
        self.elements = elements

    def sort(self):
        res_elems = copy.deepcopy(self.elements)
        n = len(res_elems)
        for it1 in range(n - 1):
            for it2 in range(it1 + 1, n):
                if res_elems[it1] > res_elems[it2]:
                    res_elems[it1], res_elems[it2] = res_elems[it2], res_elems[it1]
        return res_elems
