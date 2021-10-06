def solution(n, b):
    from numpy import base_repr
    from collections import OrderedDict

    seen = OrderedDict()

    while n not in seen:
        seen[n] = True
        x = int(''.join(sorted(n, reverse=True)), base=b)
        y = int(''.join(sorted(n)), base=b)
        z = x - y
        n = base_repr(z, base=b)

    return len(seen) - seen.keys().index(n)

if __name__ == '__main__':
    print(solution('1211', 10))
    print(solution('210022', 3))