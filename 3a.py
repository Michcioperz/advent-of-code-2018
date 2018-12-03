fabric = [[0 for _ in range(1005)] for _ in range(1005)]
with open('3.input') as f:
    for line in f:
        ident, startsize = line.strip().split(' @ ', 1)
        start, size = startsize.split(': ', 1)
        left, top = [int(x) for x in start.split(',')]
        width, height = [int(x) for x in size.split('x', 1)]
        for row in range(top, top+height):
            for cell in range(left, left+width):
                fabric[row][cell] = fabric[row][cell] + 1
print(sum(len(x) - x.count(0) - x.count(1) for x in fabric))
