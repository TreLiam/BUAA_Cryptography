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
if __name__ == '__main__':
    p = int(input())
    a = int(input())
    b = int(input())
    Ax, Ay = map(int,input().split())
    Bx, By = map(int, input().split())
    k = int(input())
    X_add,Y_add = add(Ax,Ay,Bx,By,p,a)
    X_sub,Y_sub = sub(Ax,Ay,Bx,By,p,a)
    X_mult,Y_mult = mult(Ax,Ay,p,a,k)
    X_div, Y_div = div(Bx, By, p, a, k)
    print(X_add,Y_add)
    print(X_sub,Y_sub)
    print(X_mult,Y_mult)
    print(X_div,Y_div)