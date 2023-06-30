import scipy
from scipy.stats import binom
def no_acyclic_diagrams(n):
    list = [1]

    for c in range(1, n + 1):
        a = 0
        s = 0
        for k in range(1 , c + 1):
            a = (((-1) ** (k - 1)) * (scipy.special.binom(c, k)) * (2 ** (k * (c - k))) * list[c - k])
            s = s + a
        list.append(int(s))
    print(list)


n = int(input("Please provide n: "))
no_acyclic_diagrams(n)