import typing as tp


class Heap():
    def __init__(self, array=tp.List[int]):
        self.heap = array

        self.num_changes = 0
        self.changes = []

    @property
    def size(self) -> int:
        return len(self.heap)

    @staticmethod
    def parent(pos: int) -> int:
        return ((pos + 1) // 2) - 1

    @staticmethod
    def left_child(pos: int) -> int:
        return (2 * (pos + 1)) - 1

    @staticmethod
    def right_child(pos: int) -> int:
        return (2 * (pos + 1) + 1) - 1

    def sift_up(self, pos: int) -> None:
        while pos > 0 and self.heap[self.parent(pos)] > self.heap[pos]:
            self.heap[self.parent(
                pos)], self.heap[pos] = self.heap[pos], self.heap[self.parent(pos)]

            self.num_changes += 1
            self.changes.append((self.parent(pos), pos))

            pos = self.parent(pos)

    def sift_down(self, pos: int) -> None:
        max_index = pos
        left = self.left_child(pos)
        right = self.right_child(pos)

        if left < self.size and self.heap[left] < self.heap[max_index]:
            max_index = left

        if right < self.size and self.heap[right] < self.heap[max_index]:
            max_index = right

        if pos != max_index:
            self.num_changes += 1
            self.changes.append((pos, max_index))

            self.heap[pos], self.heap[max_index] = self.heap[max_index], self.heap[pos]
            self.sift_down(max_index)

    def build(self) -> 'Heap':
        for pos in reversed(range(int(self.size / 2))):
            if self.left_child(pos) < self.size or self.right_child(pos) < self.size:
                self.sift_down(pos)
        return self


heap = Heap(array=[5, 4, 3, 2, 1]).build()
assert (heap.num_changes, heap.changes) == (3, [(1, 4), (0, 1), (1, 3)])

heap = Heap(array=[0, 1, 2, 3, 4, 5]).build()
assert (heap.num_changes, heap.changes) == (0, [])

heap = Heap(array=[7, 6, 5, 4, 3, 2]).build()
assert (heap.num_changes, heap.changes) == (
    4, [(2, 5), (1, 4), (0, 2), (2, 5)])
