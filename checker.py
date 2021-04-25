def get_all_mfas():
    for i in range(1000000):
        yield list(str(i).zfill(6))


def test_all_same(i):
    a, b, c, d, e, f = i
    return a == b and b == c and c == d and d == e and e == f


def test_aaabbb(i):
    a, b, c, d, e, f = i
    return a == b and b == c and d == e and e == f


def test_abcabc(i):
    a, b, c, d, e, f = i
    return a == d and b == e and c == f


def test_aaadef(i):
    a, b, c, d, e, f = i
    return (a == b and b == c) or (d == e and e == f)


def test_seq(i):
    #     a, b, c, d, e, f = i
    #     return a + 1 == b and a + 2 == c and a + 3 == d and a + 4 == e and a + 5 == f
    return False


def check():
    n = 0
    for i in get_all_mfas():
        if test_all_same(i) or test_aaabbb(i) or test_abcabc(i) or test_aaadef(i) or test_seq(i):
            n += 1
            print(''.join(i))
    print(n / 1000000)


if __name__ == '__main__':
    check()
