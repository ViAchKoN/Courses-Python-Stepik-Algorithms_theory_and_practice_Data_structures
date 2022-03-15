import typing as tp


def get_stack_max(command_list: tp.List[str]) -> tp.List[int]:
    result = []
    stack_max = [0]

    command: tp.Any
    for command in command_list:
        command = command.split()
        if command[0] == 'push':
            stack_max.append(max(stack_max[-1], int(command[1])))
        elif command[0] == 'pop':
            stack_max.pop()
        else:
            result.append(stack_max[-1] if stack_max else 0)
    return result


assert get_stack_max(
    command_list=[
        'push 2',
        'push 1',
        'max',
        'pop',
        'max',
    ]
) == [2, 2]
assert get_stack_max(
    command_list=[
        'push 7',
        'push 1',
        'push 7',
        'max',
        'pop',
        'max',
    ]
) == [7, 7]
assert get_stack_max(
    command_list=[
        'push 1',
        'push 2',
        'max',
        'pop',
        'max',
    ]
) == [2, 1]
assert get_stack_max(
    command_list=[
        'push 2',
        'push 3',
        'push 9',
        'push 7',
        'push 2',
        'max',
        'max',
        'max',
        'pop',
        'max',
    ]
) == [9, 9, 9, 9]
