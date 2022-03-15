import typing as tp


def inorder(tree: tp.List[tp.List[int]]) -> tp.List[int]:
    result = []

    def _traverse(pos: int):
        if pos == -1:
            return
        node = tree[pos]
        _traverse(node[1])
        result.append(node[0])
        _traverse(node[2])

    _traverse(pos=0)
    return result


def preorder(tree: tp.List[tp.List[int]]) -> tp.List[int]:
    result = []

    def _traverse(pos: int):
        if pos == -1:
            return
        node = tree[pos]
        result.append(node[0])
        _traverse(node[1])
        _traverse(node[2])

    _traverse(pos=0)
    return result


def postorder(tree: tp.List[tp.List[int]]) -> tp.List[int]:
    result = []

    def _traverse(pos: int):
        if pos == -1:
            return
        node = tree[pos]
        _traverse(node[1])
        _traverse(node[2])
        result.append(node[0])

    _traverse(pos=0)
    return result


tree = [
    [0, 7, 2],
    [10, -1, -1],
    [20, -1, 6],
    [30, 8, 9],
    [40, 3, -1],
    [50, -1, -1],
    [60, 1, -1],
    [70, 5, 4],
    [80, -1, -1],
    [90, -1, -1],
]

assert inorder(tree=tree) == [50, 70, 80, 30, 90, 40, 0, 20, 10, 60]
assert preorder(tree=tree) == [0, 70, 50, 40, 30, 80, 90, 20, 60, 10]
assert postorder(tree=tree) == [50, 80, 90, 30, 40, 70, 10, 60, 20, 0]

tree = [
    [4, 1, 2],
    [2, 3, 4],
    [5, -1, -1],
    [1, -1, -1],
    [3, -1, -1],
]

assert inorder(tree=tree) == [1, 2, 3, 4, 5]
assert preorder(tree=tree) == [4, 2, 1, 3, 5]
assert postorder(tree=tree) == [1, 3, 2, 5, 4]
