import typing as tp


def check_tree(tree: tp.List[tp.List[int]]):
    i = 0
    previous = -2**32
    previous_positions: tp.List[int] = []
    while i != -1 or previous_positions:
        key, left, right = tree[i]
        if i != -1:
            previous_positions.append(i)
            i = left
        else:
            i = previous_positions.pop()
            key, left, right = tree[i]
            if previous >= key:
                return 'INCORRECT'
            previous = key
            i = right
    return 'CORRECT'

tree = [
    [2, 1, 2],
    [1, -1, -1],
    [3, -1, -1],
]
assert check_tree(tree=tree) == 'CORRECT'

tree = [
    [1, 1, 2],
    [2, -1, -1],
    [3, -1, -1],
]
assert check_tree(tree=tree) == 'INCORRECT' 

tree = [
    [1, -1, 1],
    [2, -1, 2],
    [3, -1, 3],
    [4, -1, 4],
    [5, -1, -1],
]
assert check_tree(tree=tree) == 'CORRECT' 

tree = [
    [2, -1, 1],
    [5, 2, -1],
    [3, -1, 3],
    [5, -1, -1],
]
assert check_tree(tree=tree) == 'INCORRECT'