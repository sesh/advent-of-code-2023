def get_min_colours(game):
    game_id, turns = game.split(": ")
    turns = turns.split(";")

    red = None
    blue = None
    green = None

    for turn in turns:
        colours = [x.strip() for x in turn.split(",")]
        for colour in colours:
            num, colour = colour.split()
            num = int(num)

            if colour == "red" and (not red or num > red):
                red = num
            if colour == "green" and (not green or num > green):
                green = num
            if colour == "blue" and (not blue or num > blue):
                blue = num

    return red * blue * green


def min_cubes(fn):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        return sum([get_min_colours(l) for l in lines])


if __name__ == "__main__":
    result = min_cubes("test_01.txt")
    assert result == 2286

    result = min_cubes("input.txt")
    print("02/01:", result)
    assert result == 66027
