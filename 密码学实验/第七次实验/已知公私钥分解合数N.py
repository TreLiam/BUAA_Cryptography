import random
import gmpy2
def getpq(e,d,n):
    while True:
        k = e * d - 1
        g = random.randint(0, n)
        while k % 2 == 0:
            k = k // 2
            temp = gmpy2.powmod(g, k, n) - 1
            if gmpy2.gcd(temp, n) > 1 and temp > 1:
                return gmpy2.gcd(temp, n)
if __name__ == '__main__':
    e = int(input())
    d = int(input())
    N = int(input())
    p = getpq(e,d,N)
    q = N // p
    if p>q:
        temp = p
        p = q
        q = temp
    print(p)
    print(q)