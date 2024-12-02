with open('input.txt') as fp:
    data = [tuple(map(int, x.split(' '))) for x in fp.read().strip().splitlines()]


def is_safe(entry):
    return (
        not any(not 0 < abs(a - b) < 4 for a, b in zip(entry, entry[1:]))
        and entry in {tuple(sorted(entry)), tuple(sorted(entry, reverse=True))}
    )


# Part I
print(sum(is_safe(entry) for entry in data))

# Part II
print(sum(any(is_safe(entry[:x] + entry[x + 1:]) for x in range(len(entry))) for entry in data))
