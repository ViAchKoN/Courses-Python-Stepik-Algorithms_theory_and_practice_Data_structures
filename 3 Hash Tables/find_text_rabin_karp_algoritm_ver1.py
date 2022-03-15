import typing as tp


def find(pattern: str, text: str) -> tp.List[int]:
    result = []
    pattern_size = len(pattern)
    text_size = len(text)
    base = 263

    modulo_divider = 1000000007

    base_m = pow(base, pattern_size - 1) % modulo_divider

    pattern_hash = 0
    text_hash = 0
    for i in range(pattern_size):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % modulo_divider
        text_hash = (base * text_hash + ord(text[i])) % modulo_divider

    for i in range(text_size - pattern_size + 1):
        if pattern_hash == text_hash:
            while True:
                for j in range(pattern_size):
                    if pattern[j] != text[i + j]:
                        break
                result.append(i)
                break
        if i < text_size - pattern_size:
            text_hash = (text_hash - base_m * ord(text[i])) % modulo_divider
            text_hash = (text_hash * base + ord(text[i + pattern_size])) % modulo_divider
            text_hash = (text_hash + modulo_divider) % modulo_divider
    return result


assert find(pattern='aba', text='abacaba') == [0, 4]
assert find(pattern='Test', text='testTesttesT') == [4]
assert find(pattern='aaaaa', text='baaaaaaa') == [1, 2, 3]
