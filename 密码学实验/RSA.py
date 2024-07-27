import random

import gmpy2
from functools import reduce
import operator


# from pycallgraph import Config
# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput


def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e & 1) == 1:  # 计算e的二进制表示最低位的值
            result = (result * b) % m
        e >>= 1  # 将e右移一位，
        b = (b * b) % m  # 平方乘
    return result


def gcd(a, b):
    if a < b:
        t = a
        a = b
        b = t
    while True:
        temp = a % b
        if temp:
            a = b
            b = temp
        else:
            break
    return b


def extgcd(a, b):
    if a == 0:
        return 0, 1, b
    if b == 0:
        return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a


def miller(n):
    if n % 2 == 0:
        return 0
    temp = n - 1
    k = 0
    flag = 0
    while temp % 2 == 0:
        temp = temp // 2
        k = k + 1
    q = temp  # n-1=2^k*q
    for i in range(80):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1:
            return 0
        if pow(a, q, n) != 1:
            flag = flag + 1
        for j in range(k):
            if pow(a, (2 ** j) * q, n) != n - 1:
                flag = flag + 1

        if flag == k + 1:
            return 0
        flag = 0
    return 1
def invmod(a, n):
    if n < 2:
        raise ValueError("modulus must be greater than 1")
    x, y, g = extgcd(a, n)
    if g != 1:
        raise ValueError("no invmod for given @a and @n")
    else:
        return x % n


def solve_crt(remainders, modules):
    if len(modules) != len(remainders):
        raise TypeError("modules and remainders lists must have same len")
    if len(modules) == 0:
        raise ValueError("Empty lists are given")
    if len(modules) == 1:
        return remainders[0]

    x = 0
    N = reduce(operator.mul, modules)  # 对模数进行累积
    for i, module in enumerate(modules):
        if module == 1:
            continue

        Ni = N // module
        b = invmod(Ni, module)

        x += remainders[i] * Ni * b

    res = x % N
    if res == 0:
        return reduce(operator.mul, modules)
    else:
        return res


def enc(p, q, e, m):
    n = p * q
    return fastExpMod(m, e, n)


def dec(p, q, e, m):
    phi = (p - 1) * (q - 1)
    d = invmod(e, phi)
    d_q = d % (q - 1)
    d_p = d % (p - 1)
    Vp = fastExpMod(m, d_p, p)
    Vq = fastExpMod(m, d_q, q)
    modules = [p, q]
    remianders = [Vp, Vq]
    return solve_crt(remianders, modules)


def main():
    p = int(input())
    q = int(input())
    e = int(input())
    m = int(input())
    op = int(input())
    if miller(p) == 0 or miller(q) == 0:
        print("Mole ! Terminate !")
        return
    if op == 1:
        print(enc(p, q, e, m))
    else:
        print(dec(p, q, e, m))


if __name__ == '__main__':
    # config = Config()
    # graphviz = GraphvizOutput()
    # graphviz.output_file = 'graph.png'
    # with PyCallGraph(output=graphviz, config=config):
    main()
