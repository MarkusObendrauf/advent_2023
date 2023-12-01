print("hello world")

with open("input.txt") as f:
    lines = f.readlines()

print(lines)
words = [
    None,
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
nums = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0


def first_num(row):
    smallest_index = 99999999
    min_val = None
    for value, word in enumerate(words):
        try:
            i = row.index(word)
            if i < smallest_index:
                smallest_index = i
                min_val = value
        except:
            pass
    for value, word in enumerate(nums):
        try:
            i = row.index(word)
            if i < smallest_index:
                smallest_index = i
                min_val = value
        except:
            pass
    return min_val


def last_num(row):
    max_index = -1
    max_val = None
    for value, word in enumerate(words):
        try:
            i = row.rindex(word)
            if i > max_index:
                max_index = i
                max_val = value
        except:
            pass
    for value, word in enumerate(nums):
        try:
            i = row.rindex(word)
            if i > max_index:
                max_index = i
                max_val = value
        except:
            pass
    return max_val


for line in lines:
    n1 = first_num(line)
    n2 = last_num(line)

    print(line, n1, n2)
    sum += 10 * n1 + n2

print(sum)
