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
def encrypt(M,e,n):
    ciphertext = fastMode(M,e,n)
    return ciphertext
def decrypt(c,d,n,p,q,m):
    a = d % (p-1)
    b = d % (q-1)
    Vp = fastMode(c,a,p)
    Vq = fastMode(c,b,q)

    m = [0,0,0]
    m = exEuclid(q,p,m)
    inv_q = m[1]
    Xp = q * inv_q

    m = [0,0,0]
    m = exEuclid(p, q, m)
    inv_p = m[1]
    Xq = p * inv_p

    plaintext = (Vp * Xp + Vq * Xq) % n
    return plaintext

def RSA(p,q,e,M,op):
    n = p * q
    if op == 1:
        ciphertext = encrypt(M,e,n)
        print(ciphertext)
    else :
        m = [0,0,0]
        Euler_n = (p-1)*(q-1)
        m = exEuclid(e,Euler_n,m)
        d = m[1]
        plaintext = decrypt(M,d,n,p,q,m)
        print(plaintext)
def IsPrime(a):
    flag = 1
    m = int(pow(a,0.5))
    for i in range(2,m+1):
        if a % i == 0:
            flag = 0
            return flag
    return flag

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    e = int(input())
    M = int(input())
    op = int(input())
    if IsPrime(p) == 0:
        print("Mole ! Terminate !")
    elif IsPrime(q) == 0:
        print("Mole ! Terminate !")
    else:
        RSA(p,q,e,M,op)
