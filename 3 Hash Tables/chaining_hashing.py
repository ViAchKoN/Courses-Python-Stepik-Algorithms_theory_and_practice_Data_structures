import re
import typing as tp

MODULO_DIVIDER = 1000000007


class HashTable(list):
    def __init__(self, length: int):
        super().__init__([[] for i in range(length + 1)])

    @property
    def size(self) -> int:
        return len(self) - 1

    def add(self, text: str) -> None:
        pos = self.hash(text=text)
        if text not in self[pos]:
            self[pos].insert(0, text)

    def check(self, pos: str) -> tp.List[str]:
        return self[int(pos)] if self[int(pos)] else ' '

    def find(self, text: str) -> str:
        pos = self.hash(text=text)
        return 'yes' if text in self[pos] else 'no'

    def delete(self, text: str) -> None:
        pos = self.hash(text=text)
        for num, element in enumerate(self[pos]):
            if element == text:
                del self[pos][num]

    def hash(self, text: str) -> int:
        total = 0
        for pos, char in enumerate(list(text)):
            total += (
                ord(char) * (
                    (263**pos)
                )
            )
        return (total % MODULO_DIVIDER) % (self.size)

    def execute_command(self, command: str) -> tp.Union[str, None]:
        commands_dict = {
            'add': self.add,
            'find': self.find,
            'check': self.check,
            'del': self.delete,
        }
        for k, v in commands_dict.items():
            if re.search(r'^{0}\s+.*'.format(k), command):
                return v(command.split()[1])


def perform_actions(length: int, command_list: tp.List[str]) -> tp.List[str]:
    result: tp.List[str] = []
    hash_table = HashTable(length=length)

    for command in command_list:
        res = hash_table.execute_command(command)
        if res:
            result.append(' '.join(res) if type(res) == list else res)
    return result


assert(
    perform_actions(
        length=5,
        command_list=[
            'add world',
            'add HellO',
            'check 4',
            'find World',
            'find world',
            'del world',
            'check 4',
            'del HellO',
            'add luck',
            'add GooD',
            'check 2',
            'del good',
        ]
    )
) == [
    'HellO world',
    'no',
    'yes',
    'HellO',
    'GooD luck',
]
assert(
    perform_actions(
        length=4,
        command_list=[
            'add test',
            'add test',
            'find test',
            'del test',
            'find test',
            'find Test',
            'add Test',
            'find Test',
        ]
    )
) == [
    'yes',
    'no',
    'no',
    'yes',
]
assert(
    perform_actions(
        length=3,
        command_list=[
            'check 0',
            'find help',
            'add help',
            'add del',
            'add add',
            'find add',
            'find del',
            'del del',
            'find del',
            'check 0',
            'check 1',
            'check 2',
        ]
    )
) == [
    ' ',
    'no',
    'yes',
    'yes',
    'no',
    ' ',
    'add help',
    ' ',
]
