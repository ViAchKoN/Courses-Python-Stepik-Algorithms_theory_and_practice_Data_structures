import re
import typing as tp


class PhoneBook(list):
    def __init__(self):
        super().__init__([None] * (10**7))

    def add(self, pos: int, name: str) -> None:
        self[pos] = name

    def find(self, pos: int) -> str:
        return self[pos] if self[pos] is not None else 'not found'

    def delete(self, pos: int) -> None:
        self[pos] = None

    def execute_command(self, command: str) -> tp.Union[str, None]:
        commands_dict = {
            'add': self.add,
            'find': self.find,
            'del': self.delete,
        }
        for k, v in commands_dict.items():
            if re.search(r'^{0}\s+.*'.format(k), command):
                command = command.split()[1:]
                command[0] = int(command[0])
                return v(*command)
        return None


def perform_actions(command_list: tp.List[str]) -> tp.List[str]:
    result: tp.List[str] = []
    phone_book = PhoneBook()

    for command in command_list:
        res = phone_book.execute_command(command)
        if res:
            result.append(res)
    return result


assert(
    perform_actions(
        command_list=[
            'add 911 police',
            'add 76213 Mom',
            'add 17239 Bob',
            'find 76213',
            'find 910',
            'find 911',
            'del 910',
            'del 911',
            'find 911',
            'find 76213',
            'add 76213 daddy',
            'find 76213',
        ]
    )
) == [
    'Mom',
    'not found',
    'police',
    'not found',
    'Mom',
    'daddy',
]
assert(
    perform_actions(
        command_list=[
            'find 3839442',
            'add 123456 me',
            'add 0 granny',
            'find 0',
            'find 123456',
            'del 0',
            'del 0',
            'find 0',
        ]
    )
) == [
    'not found',
    'granny',
    'me',
    'not found',
]
