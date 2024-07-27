import math
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
def cls(num,sit):
    div = int(pow(2,32-sit))
    mult = int(pow(2,sit))
    a = num % div
    b = num // div
    result = a * mult + b
    return result
def pad(plaintext):
    tlen = len(plaintext)
    b = tlen % 512
    if b == 448:
        k = 512
    elif b < 448:
        k = 448 - b
    else:
        k = 960 - b
    padding = plaintext + "1" + (k - 1) * "0" + bin(tlen)[2:].zfill(64)
    return padding
def extend(M):
    W = []
    for i in range(16):
        W.append('0b' + M[i * 32:(i + 1) * 32])
    for i in range(16,68):
        mid = P1(eval(W[i-16]) ^ eval(W[i-9]) ^ cls(eval(W[i-3]),15)) ^ cls(eval(W[i-13]),7) ^ eval(W[i-6])
        result = bin(mid)[2:].zfill(32)
        W.append('0b' + result)
    for i in range(64):
        mid = eval(W[i]) ^ eval(W[i+4])
        result = bin(mid)[2:].zfill(32)
        W.append('0b' + result)
    return W
def FF(i,A,B,C):
    if i <= 15:
        result = A ^ B ^ C
    else:
        result = (A & B) | (A & C) | (B & C)
    return result
def GG(i,E,F,G):
    if i <= 15:
        result = E ^ F ^ G
    else:
        result = (E & F) | ((~E) & G)
    return result
def round(W,h):
    div = int(pow(2, 32))
    A,B,C,D,E,F,G,H = h
    for i in range(64):
        if i<= 15:
            T = 0x79cc4519
        else:
            T = 0x7a879d8a
        SS1 = cls((cls(A,12) + E + cls(T,i % 32)) % div,7)
        SS2 = SS1 ^ cls(A,12)
        TT1 = (FF(i,A,B,C) + D + SS2 + eval(W[i+68])) % div
        TT2 = (GG(i,E,F,G) + H + SS1 + eval(W[i])) % div
        D = C
        C = cls(B,9)
        B = A
        A = TT1
        H = G
        G = cls(F,19)
        F = E
        E = P0(TT2)
    h = [A,B,C,D,E,F,G,H]
    return h
def SM3(text):
    h = [0x7380166f, 0x4914b2b9,0x172442d7,0xda8a0600,0xa96f30bc,0x163138aa,0xe38dee4d,0xb0fb0e4e]
    EM = pad(text)
    B = []
    for i in range(len(EM)//512):
        B.append(EM[i*512:(i+1)*512])
        result = extend(B[i])
        mid = round(result,h)
        h = [mid[0]^h[0],mid[1]^h[1],mid[2]^h[2],mid[3]^h[3],mid[4]^h[4],mid[5]^h[5],mid[6]^h[6],mid[7]^h[7]]
    answer = h
    result = hex(answer[0])[2:].zfill(8) + hex(answer[1])[2:].zfill(8) + hex(answer[2])[2:].zfill(8) + hex(answer[3])[2:].zfill(8) + hex(answer[4])[2:].zfill(8) + hex(answer[5])[2:].zfill(8) + hex(answer[6])[2:].zfill(8) + hex(answer[7])[2:].zfill(8)
    return result
def P0(x):
    result = x ^ cls(x,9) ^ cls(x,17)
    return result
def P1(x):
    result = x ^ cls(x,15) ^ cls(x,23)
    return result
def backString(n,length):
    result = bin(n)[2:]
    while len(result) < length:
        result = '0' + result
    return result
def generateZA(IDA,p,a,b,Gx,Gy,xA,yA):
    t = int(math.ceil(math.log2(p)))
    l = int(math.ceil(t/8))
    lenth = 8 * l
    idA = IDA.encode("UTF-8")
    if IDA != '':
        text = int.from_bytes(idA, "big")
        text = bin(text)[2:]
        while len(text) % 8 != 0:
            text = "0" + text
    else:
        text = ''
    entlenA = len(text)
    ENTLA = backString(entlenA,16)
    the_a = backString(a,lenth)
    the_b = backString(b,lenth)
    the_Gx = backString(Gx,lenth)
    the_Gy = backString(Gy,lenth)
    the_xA = backString(xA,lenth)
    the_yA = backString(yA,lenth)
    the_String = ENTLA + text + the_a + the_b + the_Gx + the_Gy + the_xA + the_yA
    ZA = SM3(the_String)
    return ZA
def Sign_SM2(p,a,b,Gx,Gy,n,IDA,xA,yA,M,Mode):
    ZA = generateZA(IDA,p,a,b,Gx,Gy,xA,yA)
    _M = (ZA + hex(eval('0b'+M))[2:])
    lenth = len(_M)
    message = backString(eval('0x'+_M),4*lenth)
    if Mode == 'Sign':
        dA = int(input())
        K = int(input())
        e = eval('0x'+SM3(message))
        x1,y1 = mult(Gx,Gy,p,a,K)
        r = (e + x1) % n
        s = (invert(1+dA,n) * (K - r * dA))%n
        print(r)
        print(s)
    else:
        r = int(input())
        s = int(input())
        _e = eval('0x'+SM3(message))
        t = (r + s) % n
        mid1x,mid1y =  mult(Gx,Gy,p,a,s)
        mid2x,mid2y =  mult(xA,yA,p,a,t)
        _x1,_y1 = add(mid1x,mid1y,mid2x,mid2y,p,a)
        R = (_e + _x1) % n
        if (r<1) | (r > n-1):
            print('False')
        elif (s<1) | (s > n-1):
            print('False')
        elif t == 0:
            print('False')
        elif R!= r:
            print('False')
        else:
            print('True')
if __name__ == '__main__':
    p = int(input())
    a = int(input())
    b = int(input())
    Gx, Gy = map(int, input().split())
    n = int(input())
    IDA = input()
    IDA = IDA.replace('\n', '')
    IDA = IDA.replace('\r', '')
    xA,yA =  map(int, input().split())
    M = input()
    M = M.replace('\n', '')
    M = M.replace('\r', '')
    message = M.encode("UTF-8")
    if M != '':
        text = int.from_bytes(message, "big")
        text = bin(text)[2:]
        while len(text) % 8 != 0:
            text = "0" + text
    else:
        text = ''
    Mode = input()
    Sign_SM2(p, a, b, Gx, Gy, n, IDA, xA, yA, text, Mode)