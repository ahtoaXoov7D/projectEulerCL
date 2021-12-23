#!/usr/bin/env python3


def isPrime(n):
    for i in range(2, int(n**(1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def pfactors(n):
    res = []
    if isPrime(n) or n == 4:
        return [n]
    while not isPrime(n):
        for i in range(2, int(n**(1 / 2)) + 1):
            if isPrime(i) and n % i == 0:
                res.append(i)
                n = n // i
    res.append(n)
    return res


def numprod(l, default=1):
    try:
        p = l[0]
        for i in l[1:]:
            p *= i
    except IndexError:
        return default
    return p


def main():
    # create list of numbers and their prime factors
    facts = [(i, pfactors(i)) for i in range(1, 21)]

    """Goal:
    Keep only the single largest exponent for a given prime factor base.
    i.e. if we have 12 and 6 which have p. factors [2,2,3] and [2,3],
    respectively, we want [2,2,3]
    """

    counts = dict()
    for i in facts:
        for j in set(i[1]):
            if isPrime(j):
                counts.update({j: max(i[1].count(j), counts.get(j, 0))})
    out = 1
    for i in counts.items():
        out *= i[0]**i[1]
    assert out == 232792560, "incorrect"  # found answer on paper
    print(out)


if __name__ == '__main__':
    main()
