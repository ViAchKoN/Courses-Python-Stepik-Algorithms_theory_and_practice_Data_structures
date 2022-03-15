import typing as tp


BRACKETS = {
    "}": "{",
    ")": "(",
    "]": "[",
}


def check_brackets(string: str) -> tp.Union[str, int]:
    stack = []
    for index, letter in enumerate(string, start=1):
        if letter in BRACKETS.values():
            stack.append((letter, index))
        elif letter in BRACKETS.keys() and not (stack and stack.pop()[0] == BRACKETS[letter]):
            return index

    return 'Success' if not stack else stack.pop()[1]


assert check_brackets("([](){([])})") == "Success"
assert check_brackets("()[]}") == 5
assert check_brackets("{{[()]]") == 7
assert check_brackets("{{{[][][]") == 3
assert check_brackets("{*{{}") == 3
assert check_brackets("[[*") == 2
assert check_brackets("{*}") == "Success"
assert check_brackets("{{") == 2
assert check_brackets("{}") == "Success"
assert check_brackets("") == "Success"
assert check_brackets("}") == 1
assert check_brackets("*{}") == "Success"
assert check_brackets("{{{**[][][]") == 3
assert check_brackets('()({}') == 3
assert check_brackets('{{[()]}') == 1
assert check_brackets('[]') == "Success"
assert check_brackets('{}[]') == "Success"
assert check_brackets('[()]') == "Success"
assert check_brackets('(())') == "Success"
assert check_brackets('{[]}()') == "Success"
assert check_brackets('([](){([])})') == "Success"
assert check_brackets('foo(bar);') == "Success"
assert check_brackets('{') == 1
assert check_brackets('{[}') == 3
assert check_brackets('()[]}') == 5
assert check_brackets('{{[()]]') == 7
assert check_brackets('foo(bar[i);') == 10
assert check_brackets('[]([]') == 3
