# hello.py

print('hello world');

a = 3
b = 1

if a > 1:
    print('big')
    print('b의 값은', b)

    for i in range(1, 10):
        print(i)


def add(m, n):
    s = m
    s += n
    return s


def max(m, n):
    if m > n:
        return m
    else:
        return n