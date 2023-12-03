def is_valid_game(game):
    red_max = 12
    green_max = 13
    blue_max = 14
    game_id, turns = game.split(": ")
    turns = turns.split(";")

    for turn in turns:
        colours = [x.strip() for x in turn.split(",")]
        for colour in colours:
            num, colour = colour.split()
            num = int(num)

            if colour == "red" and num > red_max:
                return False
            if colour == "green" and num > green_max:
                return False
            if colour == "blue" and num > blue_max:
                return False

    return int(game_id.split()[-1])


def possible_games(fn):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        games = [is_valid_game(l) for l in lines]
        game_ids = [x for x in games if x != False]

        return sum(game_ids)


if __name__ == "__main__":
    result = possible_games("test_01.txt")
    assert result == 8

    result = possible_games("input.txt")
    print("02/01:", result)
    assert result == 3035
