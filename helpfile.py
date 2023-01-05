def f(a, b):
    c = [0] * (len(a) + len(b))
    lenc = len(a) + len(b)
    for ix in range(len(a), 0, -1):
        for jx in range(len(b), 0, -1):
            d = a[ix - 1] * b[jx - 1]
            if d > 9:
                c[ix + jx - 2] += d // 10
                c[ix + jx - 1] += d % 10
            else:
                c[ix + jx - 1] += d
        for i in range(1, lenc):
            if c[i] > 9:
                x = c[i]
                c[i - 1] += x // 10
                c[i] = x % 10
    v = 0
    h = c
    while c[v] == 0:
        v += 1
        h = c[v:]
    return h


a = [1]
for i in range(2, 101):
    j = list(str(i))
    p = [int(el) for el in j]
    a = f(a, p)
q = [str(el) for el in a]
s = ''.join(q)
print(s)

