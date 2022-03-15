import typing as tp


def get_height(tree: tp.List[int], elements_num: int) -> int:
    def _get_height(pos: int) -> int:
        node = tree[pos]
        if node == -1:
            return 1
        if node not in node_heights:
            node_heights[node] = 1 + _get_height(node)
        return node_heights[node]

    node_heights = {}
    height = 0

    for pos in range(elements_num):
        height = max(height, _get_height(pos))

    return height


assert get_height(
    tree=[9, 7, 5, 5, 2, 9, 9, 9, 2, -1],
    elements_num=10) == 4
assert get_height(
    tree=[4, -1, 4, 1, 1],
    elements_num=5) == 3
assert get_height(
    tree=[-1, 0, 4, 0, 3],
    elements_num=5) == 4
