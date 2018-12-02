import itertools
twos = 0
threes = 0
with open('2.input') as f:
    for line in f:
        counts = {len(list(y)) for x, y in itertools.groupby(sorted(line))}
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
print(twos * threes)
