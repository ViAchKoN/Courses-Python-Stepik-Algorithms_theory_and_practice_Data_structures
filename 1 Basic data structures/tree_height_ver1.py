import typing as tp

from collections import defaultdict


def get_height(node_list: tp.List[int]) -> int:
    if node_list:
        height = 1
        for node in node_list:
            height = max(height, 1 + get_height(tree[node]))
        return height
    return 0


def prepare_tree(array: tp.List[int]) -> tp.Dict[int, tp.List[int]]:
    for pos, element in enumerate(array):
        tree[element].append(pos)
    return tree


tree: tp.DefaultDict = defaultdict(list)

assert get_height(
    node_list=prepare_tree(
        array=[9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
    )[-1]) == 4
assert get_height(
    node_list=prepare_tree(
        array=[4, -1, 4, 1, 1]
    )[-1]) == 3
assert get_height(
    node_list=prepare_tree(
        array=[-1, 0, 4, 0, 3]
    )[-1]) == 4
