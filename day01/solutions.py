with open("input.txt") as f:
    data = f.read().split("\n")

l1, l2 = zip(*[map(int, x.split()) for x in data])

l1_sorted, l2_sorted = sorted(l1), sorted(l2)

result1 = sum(abs(x1 - x2) for x1, x2 in zip(l1_sorted, l2_sorted))

print(result1)

# Part 2
result2 = 0
for x in l1:
    result2 += x * l2.count(x)

print(result2)
