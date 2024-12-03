import re

with open("input.txt") as f:
    data = f.read()


def ex1():
    regex = r"(mul)\((\d+),(\d+)\)"
    result1 = 0
    for _, x, y in re.findall(regex, data):
        result1 += int(x) * int(y)

    return result1


def ex2():
    regex = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    result2 = 0
    do = True
    for w, x, y in re.findall(regex, data):
        if w == "do()":
            do = True
        elif w == "don't()":
            do = False
        else:
            if do:
                result2 += int(x) * int(y)

    return result2


print("Solution to part 1: ", ex1())

print("Solution to part 2: ", ex2())