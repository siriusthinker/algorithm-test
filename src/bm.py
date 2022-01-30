from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    pattern_len = len(pattern) - 1
    for index, element in enumerate(pattern):
        value = pattern_len - index
        table[element] = value

    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        if self.table.get(c):
            return self.table.get(c)
        return -1

    def search(self) -> int:
        pattern_len = len(self.pattern) - 1
        i = pattern_len

        while i < len(self.text):
            j = pattern_len
            while j >= 0 and self.text[i] == self.pattern[j]:
                i -= 1
                j -= 1
            if j < 0:
                return i + 1

            shift = self.decide_slide_width(self.text[i])
            if shift != -1:
                i += shift
            else:
                i += pattern_len
        return -1
