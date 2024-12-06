from functools import cmp_to_key

with open('input.txt') as fp:
    data = fp.read().strip()
    constraints = sorted(tuple(map(int, x.split('|'))) for x in data.split('\n\n')[0].splitlines())
    updates = [list(map(int, x.split(','))) for x in data.split('\n\n')[1].splitlines()]

part1, part2 = 0, 0
for update in updates:
    original = update.copy()
    while update:
        item = update.pop(0)
        if {(remaining, item) for remaining in update} & set(constraints):
            corrected = list(
                sorted(original, key=cmp_to_key(lambda a, b: -1 if (a, b) in constraints else 0))
            )
            part2 += corrected[len(corrected) // 2]
            break
    part1 += original[len(original) // 2] if not update else 0

print(f'{part1}\n{part2}')
