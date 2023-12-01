def first_numeric(s, reversed=False):
    for i, c in enumerate(s):
        if c in "1234567890":
            return c

        for j, num in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if reversed:
                num = num[::-1]
            if s[i : i + len(num)] == num:
                print(num)
                return str(j + 1)


def sum_first_last(fn):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

        values = []
        for line in lines:
            i = first_numeric(line) + first_numeric(line[::-1], reversed=True)
            values.append(int(i))

    return sum(values)


if __name__ == "__main__":
    result = sum_first_last("test_02.txt")
    assert result == 281

    result = sum_first_last("input.txt")
    print("01/02:", result)
    assert result == 54078
