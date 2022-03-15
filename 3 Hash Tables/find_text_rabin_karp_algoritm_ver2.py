import typing as tp


def find(pattern: str, text: str) -> tp.List[int]:
    result = []
    pattern_size = len(pattern)
    text_size = len(text)
    base = 263

    modulo_divider = 1000000007

    base_m_dict = {0: 1}
    for i in range(1, pattern_size):
        base_m_dict[i] = (base_m_dict[i - 1] * base) % modulo_divider

    pattern_hash = 0
    text_hash = 0
    for i in reversed(range(pattern_size)):
        pattern_hash += (
            ord(pattern[pattern_size - 1 - i]) * base_m_dict[i]
        )
        text_hash += (
            ord(text[pattern_size - 1 - i]) * base_m_dict[i]
        )
    pattern_hash %= modulo_divider
    text_hash %= modulo_divider

    for i in range(text_size - pattern_size + 1):
        if pattern_hash == text_hash:
            while True:
                for j in range(pattern_size):
                    if pattern[j] != text[i + j]:
                        break
                result.append(i)
                break
        if i < text_size - pattern_size:
            test_hash = 0
            for j in reversed(range(pattern_size)):
                test_hash += (
                    ord(text[i + pattern_size - j]) * base_m_dict[j]
                )
            test_hash %= modulo_divider

            text_hash = (text_hash - base_m_dict[pattern_size - 1] * ord(text[i]) % modulo_divider) % modulo_divider
            text_hash = (text_hash * base + ord(text[i + pattern_size])) % modulo_divider
            text_hash = (text_hash + modulo_divider) % modulo_divider
    return result


assert find(pattern='aba', text='abacaba') == [0, 4]
assert find(pattern='Test', text='testTesttesT') == [4]
assert find(pattern='aaaaa', text='baaaaaaa') == [1, 2, 3]
