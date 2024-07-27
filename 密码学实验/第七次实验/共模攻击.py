import gmpy2
def exEuclid(a,b,m):
    if b == 0:
        m[0] = a
        m[1] = 1
        m[2] = 0
        return m
    else:
        exEuclid(b,a%b,m)
        GCD = m[0]
        xtmp = m[1]
        ytmp = m[2]
        x = ytmp
        y = xtmp - (a//b) * ytmp
        if GCD < 0:
            x = -x
            y = -y
            GCD = -GCD
        while x <= 0:
            x += abs(b) // GCD
            y = (GCD - a*x) // b
        m[0] = GCD
        m[1] = x
        m[2] = y
        return m
def fastMode(base,expo,p):
    ans = 1
    while expo > 0:
        a = expo % 2
        expo = expo >> 1
        if a == 1:
            ans = (ans * base) % p
        base = (base * base) % p
    return ans
def Mod_Attack(e1,e2,c1,c2,n):
    m = [0,0,0]
    m = exEuclid(e1,e2,m)
    r = m[1]
    s = m[2]
    p = (gmpy2.powmod(c1, r, n)*gmpy2.powmod(c2, s, n))%n
    return p
if __name__ == '__main__':
    e1 = int(input())
    e2 = int(input())
    c1 = int(input())
    c2 = int(input())
    N = int(input())
    print(Mod_Attack(e1,e2,c1,c2,N))