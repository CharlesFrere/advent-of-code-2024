import numpy as np

with open("input.txt") as file:
    matrix = np.array([list(line.strip()) for line in file])

rows, cols = matrix.shape
word = "XMAS"

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]


def is_xmas(r, c, dr, dc):
    for i in range(len(word)):
        nr, nc = r + i * dr, c + i * dc
        if not (0 <= nr < rows and 0 <= nc < cols) or matrix[nr][nc] != word[i]:
            return False
    return True


def ex1():
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if is_xmas(r, c, dr, dc):
                    count += 1

    return count


def is_cross_xmas(r, c):
    if matrix[r][c] == "A":
        ul, ur, bl, br = matrix[r+1][c-1], matrix[r+1][c+1], matrix[r-1][c-1], matrix[r-1][c+1]
        if {ul, br} == {"M", "S"}:
            if {ur, bl} == {"M", "S"}:
                return True

    return False


def ex2():
    count = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if is_cross_xmas(r, c):
                count += 1

    return count


print("Total occurrences of 'XMAS':", ex1())

print("Total occurrences of 'CROSS_XMAS':", ex2())
