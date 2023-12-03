import itertools
import functools
import math


with open("input.txt") as f:
    lines = f.readlines()

grid = [[] for _ in range(len(lines))]
grid = [list(line.strip()) for line in lines]


def get_number_coords(lines) -> list[list[tuple]]:
    num_coords = []
    for row_n, row in enumerate(grid):
        in_number = False
        for col_n, col in enumerate(row):
            if col.isdigit():
                if not in_number:
                    in_number = True
                    num_coords.append([(row_n, col_n), (row_n, len(row))])
            else:
                if in_number:
                    in_number = False
                    num_coords[-1][1] = (row_n, col_n)
                continue
    return num_coords


def has_neighbour(grid, coords: list[tuple[int]]):
    start, end = coords
    start_row_n, start_col_n = start
    end_row_n, end_col_n = end
    assert start_row_n == end_row_n
    assert start_col_n < end_col_n
    s_row = max(0, start_row_n - 1)
    e_row = min(len(grid) - 1, end_row_n + 1)
    s_col = max(0, start_col_n - 1)
    e_col = min(len(grid[0]) - 1, end_col_n)

    for i in range(s_row, e_row + 1):
        for j in range(s_col, e_col + 1):
            element = grid[i][j]
            if not element.isdigit():
                if not element == ".":
                    return True
    return False


def parse_n(grid, coords):
    start, end = coords
    start_row_n, start_col_n = start
    end_row_n, end_col_n = end
    n = 0
    for col in range(start_col_n, end_col_n):
        n *= 10
        n += int(grid[start_row_n][col])
    return n


answer = 0
num_coords = get_number_coords(lines)
for n in num_coords:
    print(n)
    if has_neighbour(grid, n):
        value = parse_n(grid, n)
        answer += value

print(answer)
