import itertools as it

with open('input.txt') as fp:
    data = fp.read().strip().splitlines()

grid = {(x, y): data[y][x] for (x, y) in it.product(range(len(data[0])), range(len(data)))}

# Part I
part1 = sum(
    sum(1 for (r, s) in it.product(*([[-1, 0, 1]] * 2)) if (
            grid.get((x + r, y + s), '') +
            grid.get((x + (r * 2), y + (s * 2)), '') +
            grid.get((x + (r * 3), y + (s * 3)), '')
        ) == 'MAS'
    ) for (x, y) in ((a, b) for (a, b), l in grid.items() if l == 'X')
)
print(part1)

# Part II
part2 = sum(1 for (x, y) in ((a, b) for (a, b), l in grid.items() if l == 'A') if (''.join([
    grid.get((x - 1, y - 1), ''),
    grid.get((x + 1, y - 1), ''),
    grid.get((x - 1, y + 1), ''),
    grid.get((x + 1, y + 1), ''),
]) in {'MMSS', 'MSMS', 'SSMM', 'SMSM'}))
print(part2)
