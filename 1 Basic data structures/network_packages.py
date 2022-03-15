import typing as tp

from collections import deque


def process_packages(size: int, package_list: tp.List[tp.Tuple[int, int]]) -> tp.List[int]:
    result = []
    processing_queue: tp.Deque[int] = deque()
    for package in package_list:
        start, duration = package

        if processing_queue and start >= processing_queue[-1]:
            processing_queue.pop()

        if len(processing_queue) != size:
            start = processing_queue[0] if processing_queue else start
            result.append(start)
            processing_queue.appendleft(duration + start)
            continue

        result.append(-1)
    return result


assert process_packages(
    size=2,
    package_list=[
        (1, 100),
        (1, 100),
        (1, 0),
    ]
) == [1, 101, -1]
assert process_packages(
    size=2,
    package_list=[
        (0, 0),
        (0, 0),
        (0, 0),
        (1, 0),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
    ]
) == [0, 0, 0, 1, 1, 1, 2, -1]
assert process_packages(
    size=3,
    package_list=[
        (0, 7),
        (0, 0),
        (2, 0),
        (3, 3),
        (4, 0),
        (5, 0),
    ]
) == [0, 7, 7, -1, -1, -1]
assert process_packages(
    size=2,
    package_list=[
        (2, 9),
        (4, 8),
        (10, 9),
        (15, 2),
        (19, 1),
    ]
) == [2, 11, -1, 19, 21]
assert process_packages(
    size=1,
    package_list=[
        (999999, 1),
        (1000000, 0),
        (1000000, 1),
        (1000000, 0),
        (1000000, 0),
    ]
) == [999999, 1000000, 1000000, -1, -1]
assert process_packages(
    size=3,
    package_list=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
    ]
) == [1, 2, 4, 7, 11, -1, 16, -1]
