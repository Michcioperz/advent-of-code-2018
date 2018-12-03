claims = []
with open('3.input') as f:
    for line in f:
        ident, startsize = line.strip().split(' @ ', 1)
        start, size = startsize.split(': ', 1)
        left, top = [int(x) for x in start.split(',')]
        width, height = [int(x) for x in size.split('x', 1)]
        claims.append((ident, left, top, width, height))

print(claims)

def two_nonovl(lhs, rhs):
    if lhs[0] == rhs[0]:
        return True
    left = max(lhs[1], rhs[1])
    right = min(lhs[1]+lhs[3], rhs[1]+rhs[3])
    if not (left < right):
        return True 
    top = max(lhs[2], rhs[2])
    bottom = min(lhs[2]+lhs[4], rhs[2]+rhs[4])
    if not (top < bottom):
        return True
    return False

for claim in claims:
    if all(two_nonovl(claim, other) for other in claims):
        print(claim)
