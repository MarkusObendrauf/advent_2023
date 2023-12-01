with open("input.txt") as f:
    lines = f.readlines()


def parse_draws(line) -> list[dict[str, int]]:
    parsed = []
    line = line.split(": ")[1]
    draws_raw = line.split("; ")
    for draw_raw in draws_raw:
        color_counts = draw_raw.split(", ")
        counts = {}
        for color_count in color_counts:
            for color in ["red", "blue", "green"]:
                if color in color_count:
                    counts[color] = int(color_count.split(" ")[0])
        parsed.append(counts)
    return parsed


def power(draws):
    product = 1
    for color in ("red", "green", "blue"):
        max_in_game = max(draw.get(color, 0) for draw in draws)
        product *= max_in_game
    return product


answer = 0
for i, line in enumerate(lines):
    line_number = i + 1
    print(line)
    draws = parse_draws(line)
    draw_power = power(draws)
    print(draw_power)
    answer += draw_power


print(answer)
