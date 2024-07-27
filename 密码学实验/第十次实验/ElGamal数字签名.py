from hashlib import sha256
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
def Sign_ElGamal(q,a,m,Mode):
    if Mode == 'Sign':
        XA = int(input())
        K = int(input())
        S1 = fastMode(a,K,q)
        mlist = [0,0,0]
        mlist = exEuclid(K,q-1,mlist)
        _K = mlist[1]
        S2 = (_K*(m - XA * S1))%(q-1)
        print(S1,S2)
    else:
        YA = int(input())
        S1,S2 = map(int, input().split())
        V1 = fastMode(a,m,q)
        V2 = (fastMode(YA,S1,q)*fastMode(S1,S2,q))%q
        if V1 == V2:
            print('True')
        else:
            print('False')
if __name__ == '__main__':
    q = int(input())
    a = int(input())
    M = input()
    M = M.replace('\n', '')
    M = M.replace('\r', '')
    m = eval('0x'+sha256(M.encode('utf-8')).hexdigest())
    Mode = input()
    Sign_ElGamal(q,a,m,Mode)
