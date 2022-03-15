import typing as tp


def sliding_window_max(window_size: int, array: tp.List[int]) -> int:
    input_stack = []
    output_stack = []
    result = []

    max_input_stack = 0

    i = 0
    while i < len(array):
        number = array[i]
        if len(input_stack) != window_size:

            if output_stack:
                max_number = output_stack.pop()[1]
                result.append(max(max_number, max_input_stack, number))

            input_stack.append(number)
            max_input_stack = max(max_input_stack, input_stack[-1])

            i += 1
            continue
        else:
            while input_stack:
                input_number = input_stack.pop()

                max_number = max(
                    output_stack[-1][1], input_number) if output_stack else input_number

                output_stack.append(
                    (input_number, max_number)
                )

            max_input_stack = 0
            result.append(output_stack.pop()[1])

    if len(input_stack) == window_size:
        result.append(max_input_stack)
    return result


assert sliding_window_max(
    window_size=4,
    array=[2, 7, 3, 1, 5, 2, 6, 2]
) == [7, 7, 5, 6, 6]
assert sliding_window_max(
    window_size=1,
    array=[2, 1, 5]
) == [2, 1, 5]
assert sliding_window_max(
    window_size=7,
    array=[73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16]
) == [73, 97, 97, 97, 97, 97, 97, 97, 42]
assert sliding_window_max(
    window_size=12,
    array=[28, 7, 64, 40, 68, 86, 80, 93, 4, 53, 32, 56, 68, 18, 59]
) == [93, 93, 93, 93]
assert sliding_window_max(
    window_size=5,
    array=[27, 83, 29, 77, 6, 3, 48, 2, 16, 72, 46, 38, 55, 2, 58, ]
) == [83, 83, 77, 77, 48, 72, 72, 72, 72, 72, 58]
