def main():
    with open('2.input') as f:
        lines = [x.strip() for x in f]

    n = len(lines)
    l = len(lines[0])

    for j in range(l):
        commons = set()
        for data in lines:
            if data[:j] + data[j+1:] in commons:
                return data[:j] + data[j+1:]
            commons.add(data[:j] + data[j+1:])

print(main())
