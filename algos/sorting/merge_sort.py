import typing as t


class MergeSort:
    def __init__(self, elements: t.List):
        self.elements = elements

    def _split(self, elems):
        middle = len(elems) // 2
        return elems[:middle], elems[middle:]

    def _merge(self, left, right):
        result_arr = []
        it1, it2 = 0, 0
        while it1 < len(right) and it2 < len(left):
            if right[it1] < left[it2]:
                result_arr.append(right[it1])
                it1 += 1
            else:
                result_arr.append(left[it2])
                it2 += 1
        if it1 == len(right) and it2 < len(left):
            result_arr.extend(left[it2:])
        elif it2 == len(left) and it1 < len(right):
            result_arr.extend(right[it1:])
        return result_arr

    def _wrapper(self, els):
        if len(els) > 1:
            left, right = self._split(els)
            return self._merge(self._wrapper(left), self._wrapper(right))
        else:
            return els

    def sort(self):
        return self._wrapper(self.elements)
