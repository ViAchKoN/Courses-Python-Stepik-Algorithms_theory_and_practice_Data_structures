import typing as tp


class DisjointSet(list):
    def __init__(self, ranks: tp.List[int]):
        super().__init__([n for n in range(len(ranks))])
        self.ranks = ranks
        self.max_rank = max(self.ranks)

    def find(self, num: int) -> int:
        if num == self[num]:
            return num
        return self.find(self[num])

    def union(self, num1: int, num2: int) -> None:
        set1 = self.find(num1)
        set2 = self.find(num2)

        if set1 != set2:
            if self.ranks[set2] > self.ranks[set1]:
                set1, set2 = set2, set1

            self[set2] = set1
            self.ranks[set1] += self.ranks[set2]

            if self.ranks[set1] > self.max_rank:
                self.max_rank = self.ranks[set1]


def perform_unions(ranks: tp.List[int], command_list: tp.List[tp.Tuple[int, int]]) -> tp.List[int]:
    disjoint_set = DisjointSet(ranks=ranks)

    result: tp.List[int] = []

    for command in command_list:
        disjoint_set.union(*tuple(map(lambda x: x - 1, command)))
        result.append(disjoint_set.max_rank)
    return result


assert perform_unions(
    ranks=[1, 1, 1, 1, 1],
    command_list=[
        (3, 5),
        (2, 4),
        (1, 4),
        (5, 4),
        (5, 3),
    ],
) == [2, 2, 3, 5, 5]
assert perform_unions(
    ranks=[10, 0, 5, 0, 3, 3],
    command_list=[
        (6, 6),
        (6, 5),
        (5, 4),
        (4, 3),
    ],
) == [10, 10, 10, 11]
