with open("input.txt") as f:
    data = f.read().split("\n")


def is_sorted(l):
    return sorted(l) == l or sorted(l, reverse=True) == l


def is_safe(l):
    distances = [abs(a - b) for a, b in zip(l[0:len(l) - 1], l[1:len(l)])]
    if sum([1 for i in distances if i > 3 or i == 0]) == 0 and is_sorted(l):
        return True
    return False


def ex1():
    result1 = 0
    for line in data:
        l = list(map(int, line.split()))
        if is_safe(l):
            result1 += 1

    return result1


def ex2():
    result2 = 0
    for line in data:
        l = list(map(int, line.split()))
        if any(is_safe(l[:i] + l[i+1:]) for i in range(len(l))):
            result2 += 1

    return result2


if __name__ == "__main__":
    print("Solution to part 1: ", ex1())

    print("Solution to part 2: ", ex2())

