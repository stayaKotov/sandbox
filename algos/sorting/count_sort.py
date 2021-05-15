import typing as t


class CountSort:
    def __init__(self, elements: t.List):
        self.elements = elements

    def sort(self):
        el_2_count = {}
        result = []
        for el in self.elements:
            if el not in el_2_count.keys():
                el_2_count[el] = 1
            else:
                el_2_count[el] += 1
        tpl = [(k, v) for k, v in el_2_count.items()]
        tpl = sorted(tpl, key=lambda x: x[0])
        for k, v in tpl:
            result += [k for _ in range(v)]
        return result
