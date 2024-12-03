import re

with open('input.txt') as fp:
    data = fp.read().strip()

print('\n'.join(
    str(sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', x)))
    for x in (data, ''.join(map(lambda x: x.split('don\'t()')[0], f'do(){data}'.split('do()'))))
))
