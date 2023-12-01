def first_numeric(s):
    for c in s:
        if c in "1234567890":
            return c


def sum_first_last(fn):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

        values = []
        for line in lines:
            i = first_numeric(line) + first_numeric(line[::-1])
            values.append(int(i))

    return sum(values)


if __name__ == "__main__":
    result = sum_first_last("test_01.txt")
    assert result == 142

    result = sum_first_last("input.txt")
    print("01/01:", result)
    assert result == 54601
