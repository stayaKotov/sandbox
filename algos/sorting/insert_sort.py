import typing as t
import copy


class InsertSort:
    def __init__(self, elements: t.List):
        self.elements = elements

    def sort(self):
        res_elems = copy.deepcopy(self.elements)
        n = len(res_elems)
        for i in range(1, n):
            cur_elem = res_elems[i]
            j = i-1
            while j >= 0:
                if cur_elem < res_elems[j]:
                    res_elems[j+1] = res_elems[j]
                    j -= 1
                    if j == -1:
                        res_elems[0] = cur_elem
                        break
                else:
                    res_elems[j + 1] = cur_elem
                    break
        return res_elems
