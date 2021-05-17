import typing as t


class QuickSort:
    def __init__(self, elements: t.List):
        self.elements = elements

    def _find_anchor(self, ar):
        middle = len(ar)//2
        return middle, ar[middle]

    def replace(self, ar):
        if len(ar) < 2:
            return ar
        if len(ar) == 2:
            return ar if ar[0] < ar[1] else [ar[1], ar[0]]
        anchor_index, anchor = self._find_anchor(ar)
        i, j = 0, len(ar)-1
        res1, res2 = [], []
        while i < anchor_index < j:
            el1, el2 = ar[i], ar[j]
            if el1 <= anchor:
                res1.append(el1)
            else:
                res2.append(el1)
            i += 1
            if el2 <= anchor:
                res1.append(el2)
            else:
                res2.append(el2)
            j -= 1
        if i < anchor_index:
            for ix in range(i, anchor_index):
                if ar[ix] > anchor:
                    res2.append(ar[ix])
                else:
                    res1.append(ar[ix])
        if j > anchor_index:
            for ix in range(j, anchor_index, -1):
                if ar[ix] > anchor:
                    res2.append(ar[ix])
                else:
                    res1.append(ar[ix])
        result = self.replace(res1) + [anchor] + self.replace(res2)
        return result

    def sort(self):
        return self.replace(self.elements)
