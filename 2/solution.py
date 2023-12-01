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


def draws_are_possible(draws, cube_limits):
    for color, limit in cube_limits.items():
        for draw in draws:
            if draw.get(color, 0) > cube_limits[color]:
                return False
    return True


answer = 0
for i, line in enumerate(lines):
    line_number = i + 1
    print(line)
    draws = parse_draws(line)
    cube_limits = {"red": 12, "green": 13, "blue": 14}
    if draws_are_possible(draws, cube_limits):
        print("fit")
        answer += line_number


print(answer)
