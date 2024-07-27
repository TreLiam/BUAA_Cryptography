import hashlib
import math
def Hash(res):
    if len(res) % 2 != 0:
        res = '0' + res
    sha = hashlib.sha256(bytearray.fromhex(res))
    encrypts = sha.hexdigest()
    return encrypts
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
def transTheSet(x,y,Par):
    midx = hex(x)[2:]
    midy = hex(y)[2:]
    if len(midx) < (Par//4):
        midx = '0' + midx
    if len(midy) < (Par//4):
        midy = '0' + midy
    return midx,midy
def backString(n,length):
    result = hex(n)[2:]
    while len(result) < length:
        result = '0' + result
    return result
def KDF(Z,klen):
    counter = 1
    time = klen // 64
    if klen % 64 != 0:
        time += 1
    Ha = []
    for i in range(time):
        s = backString(counter,8)
        c = Z+s
        Ha.append(Hash(c))
        counter+=1
    if klen % 64 != 0:
        Ha[time-1] = Ha[time-1][0:(klen - (64 * (klen // 64)))]
    result = ''
    for i in range(len(Ha)):
        result = result + Ha[i]
    return '0x'+result
def SM2_Exchange(User,p,a,b,Gx,Gy,n,IDA,IDB,d,PAx,PAy,PBx,PBy,r,Rx,Ry,Par,h,klen):
    w = math.ceil(math.ceil(math.log2(n))/2) - 1
    the_w = int(pow(2,w))
    #计算ZA ZB
    entlenA = len(IDA) * 4
    ENTLA = backString(entlenA,4)
    entlenB = len(IDB) * 4
    ENTLB = backString(entlenB,4)
    t = math.ceil(math.log2(p))
    length = math.ceil(t / 8) * 2
    the_a = backString(a, length)
    the_b = backString(b, length)
    xG = backString(Gx,length)
    yG = backString(Gy,length)
    xA = backString(PAx, length)
    yA = backString(PAy, length)
    xB = backString(PBx, length)
    yB = backString(PBy, length)
    ZA = Hash(ENTLA+IDA+the_a+the_b+xG+yG+xA+yA)
    ZB = Hash(ENTLB+IDB+the_a+the_b+xG+yG+xB+yB)
    if User == 'A':
        dA = d
        rA = r
        RAx,RAy = mult(Gx,Gy,p,a,rA)
        x1 = RAx
        y1 = RAy
        RBx,RBy = Rx,Ry
        x2 = RBx
        y2 = RBy
        #计算_x1,tA
        _x1 = the_w + (x1 & (the_w - 1))
        tA = (dA + _x1 * rA) % n
        #计算_x2,U
        _x2 = the_w + (x2 & (the_w - 1))
        midx,midy = mult(RBx,RBy,p,a,_x2)
        midwayx,midwayy = add(midx,midy,PBx,PBy,p,a)
        Ux,Uy = mult(midwayx,midwayy,p,a,h * tA)
        xU,yU = transTheSet(Ux,Uy,Par)
        #计算KA，S1
        KA = KDF(xU+yU+ZA+ZB,klen)
        x1_string = backString(x1, length)
        x2_string = backString(x2, length)
        y1_string = backString(y1, length)
        y2_string = backString(y2, length)
        S1 = Hash('02'+yU+ Hash(xU+ZA+ZB+x1_string+y1_string+x2_string+y2_string))
        #计算SA
        SA = Hash('03'+yU+ Hash(xU+ZA+ZB+x1_string+y1_string+x2_string+y2_string))
        print(eval(KA))
        print(eval('0x'+S1),eval('0x'+SA))
    else:
        dB = d
        rB = r
        RBx, RBy = mult(Gx, Gy, p, a, rB)
        RAx, RAy = Rx, Ry
        x1 = RAx
        y1 = RAy
        x2 = RBx
        y2 = RBy
        #计算_x2,tB
        _x2 = the_w + (RBx & (the_w - 1))
        tB = (dB + _x2 * rB) % n
        #计算_x1,V
        _x1 = the_w + (x1 & (the_w - 1))
        midx, midy = mult(RAx, RAy, p, a, _x1)
        midwayx, midwayy = add(midx, midy, PAx, PAy, p, a)
        Vx, Vy = mult(midwayx, midwayy, p, a, h * tB)
        xV, yV= transTheSet(Vx, Vy, Par)
        #计算KB，SB
        KB = KDF(xV+yV+ZA+ZB,klen)
        x1_string = backString(x1, length)
        x2_string = backString(x2, length)
        y1_string = backString(y1, length)
        y2_string = backString(y2, length)
        SB = Hash('02' + yV + Hash(xV + ZA + ZB + x1_string + y1_string + x2_string + y2_string))
        #计算S2
        S2 = Hash('03' + yV + Hash(xV + ZA + ZB + x1_string + y1_string + x2_string + y2_string))
        print(eval(KB))
        print(eval('0x' + SB), eval('0x' + S2))
if __name__ == '__main__':
    User = input()
    p = int(input())
    a = int(input())
    b = int(input())
    Gx,Gy = map(int,input().split())
    n = int(input())
    IDA = input()
    IDB = input()
    d = int(input())
    xA, yA = map(int, input().split())
    xB, yB = map(int,input().split())
    r = int(input())
    Rx,Ry = map(int,input().split())
    Par = 256
    h = 1
    klen = 32
    SM2_Exchange(User,p,a,b,Gx,Gy,n,IDA,IDB,d,xA,yA,xB,yB,r,Rx,Ry,Par,h,klen)