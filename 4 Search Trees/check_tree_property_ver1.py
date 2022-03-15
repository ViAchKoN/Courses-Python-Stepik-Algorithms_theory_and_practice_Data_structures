import typing as tp


def check_tree(tree: tp.List[tp.List[int]]):
    previous = None
    def _inorder_traverse(pos: int):
        nonlocal previous
        if pos == -1:
            return
        key, left, right = tree[pos]
        if _inorder_traverse(left) == False:
            return False
        if previous and previous >= key:
            return False
        previous = key 
        if _inorder_traverse(right) == False:
            return False
    if _inorder_traverse(pos=0) == False:
        return 'INCORRECT' 
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

