import typing as tp


class DisjointSet(list):
    def __init__(self, length: int):
        super().__init__([n for n in range(length)])

    def find(self, num: int) -> int:
        if num == self[num]:
            return num
        return self.find(self[num])

    def union(self, num1: int, num2: int) -> None:
        parent = self.find(num1)
        while parent != self[num2]:
            self[num2], num2 = parent, self[num2]


def perform_analysis(
    length: int,
    equal_cnt: int,
    not_equal_cnt: int,
    equality_list: tp.List[tp.Tuple[int, int]],
) -> int:
    disjoint_set = DisjointSet(length=length)

    equality_list = [(i - 1, j - 1) for i, j in equality_list]
    for i in range(equal_cnt):
        disjoint_set.union(*equality_list[i])

    for i in range(equal_cnt, equal_cnt + not_equal_cnt):
        x, y = equality_list[i]
        if disjoint_set[x] == disjoint_set[y]:
            return 0
    return 1


assert perform_analysis(
    length=4,
    equal_cnt=6,
    not_equal_cnt=1,
    equality_list=[
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4),
        (1, 2)
    ],
) == 0
assert perform_analysis(
    length=4,
    equal_cnt=6,
    not_equal_cnt=0,
    equality_list=[
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4),
    ],
) == 1
assert perform_analysis(
    length=6,
    equal_cnt=5,
    not_equal_cnt=3,
    equality_list=[
        (2, 3),
        (1, 5),
        (2, 5),
        (3, 4),
        (4, 2),
        (6, 1),
        (4, 6),
        (4, 5)
    ],
) == 0
assert perform_analysis(
    length=15,
    equal_cnt=5,
    not_equal_cnt=3,
    equality_list=[
        (6, 9),
        (2, 3),
        (5, 9),
        (4, 8),
        (1, 12),
        (15, 9),
        (3, 8),
        (6, 8)
    ],
) == 1
