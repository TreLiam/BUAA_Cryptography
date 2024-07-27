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
def invert(a,b):
    m = [0,0,0]
    result = exEuclid(a,b,m)
    return result[1]
def add(Ax,Ay,Bx,By,p,a):
    if (Ax == Bx)&(Ay == By):
        m = ((3 * Ax * Ax + a)*invert(2*Ay,p)) % p
    else:
        m = ((By - Ay) * invert(Bx - Ax, p)) % p
    Rx = (m * m - Ax - Bx) % p
    Ry = (m*(Ax - Rx) - Ay) % p
    return Rx,Ry
def sub(Ax,Ay,Bx,By,p,a):
    if (Ax == Bx)&(Ay == By):
        Rx,Ry = 0,0
    else:
        Rx,Ry = add(Ax,Ay,Bx,p-By,p,a)
    return Rx,Ry
def mult(Ax,Ay,p,a,k):
    flag = 0
    Rx,Ry= 0,0
    Qx,Qy= Ax,Ay
    while k>0:
        if k % 2 == 1:
            if flag == 0:
                flag = 1
                Rx,Ry = Qx,Qy
            else:
                Rx,Ry = add(Rx,Ry,Qx,Qy,p,a)
        Qx,Qy = add(Qx,Qy,Qx,Qy,p,a)
        k = k // 2
    return Rx,Ry
def div(Bx,By,p,a,k):
    r = invert(k,p)
    Rx,Ry = mult(Bx,By,p,a,r)
    return Rx,Ry
def encrypt(p,a,b,Gx,Gy,Pmx,Pmy,k,Pbx,Pby):
    C1x,C1y = mult(Gx,Gy,p,a,k)
    midx,midy = mult(Pbx,Pby,p,a,k)
    C2x,C2y = add(Pmx,Pmy,midx,midy,p,a)
    return C1x,C1y,C2x,C2y
def decrypt(p,a,b,Gx,Gy,C1x, C1y,C2x, C2y,nB):
    midx, midy = mult(C1x, C1y, p, a, nB)
    Pmx, Pmy = sub(C2x,C2y,midx,midy,p,a)
    print(Pmx,Pmy)
def ECC(p,a,b,op,Gx,Gy):
    if op == 1:
        Pmx,Pmy = map(int,input().split())
        k = int(input())
        Pbx,Pby = map(int,input().split())
        C1x, C1y, C2x, C2y = encrypt(p,a,b,Gx,Gy,Pmx,Pmy,k,Pbx,Pby)
        print(C1x,C1y)
        print(C2x,C2y)
    else:
        C1x, C1y = map(int, input().split())
        C2x, C2y = map(int, input().split())
        nB = int(input())
        decrypt(p,a,b,Gx,Gy,C1x, C1y,C2x, C2y,nB)


if __name__ == '__main__':
    p = int(input())
    a = int(input())
    b = int(input())
    Gx,Gy = map(int,input().split())
    op = int(input())
    ECC(p,a,b,op,Gx,Gy)
