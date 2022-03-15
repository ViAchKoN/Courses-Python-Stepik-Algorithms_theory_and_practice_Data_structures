import typing as tp
from heapq import heappush, heappop


def process(num_processors: int, tasks_list: tp.List[int]) -> tp.List[tp.Tuple[int, int]]:
    result: tp.List = []

    heap: tp.List = [[0, n] for n in range(num_processors)]
    for task in tasks_list:
        processor = heappop(heap)
        result.append((processor[1], processor[0]))
        processor[0] += task
        heappush(heap, processor)

    return result


assert process(
    num_processors=2,
    tasks_list=[1, 2, 3, 4, 5]
) == [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

assert process(
    num_processors=4,
    tasks_list=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
) == [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 2),
    (0, 3),
    (1, 3),
    (2, 3),
    (3, 3),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
]
