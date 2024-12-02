with open('input.txt') as fp:
    left, right = zip(*[tuple(map(int, x.split('   '))) for x in fp.read().strip().splitlines()])

# Part I
print(sum(abs(a - b) for a, b in zip(sorted(left), sorted(right))))

# Part II
print(sum(x * (right.count(x)) for x in left))
