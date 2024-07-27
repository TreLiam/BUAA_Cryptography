import hashlib
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
def backString(n):
    result = hex(n)[2:]
    while len(result) < 8:
        result = '0' + result
    return result
def KDF(Z,klen):
    counter = 1
    time = klen // 64
    if klen % 64 != 0:
        time += 1
    Ha = []
    for i in range(time):
        s = backString(counter)
        c = Z+s
        Ha.append(Hash(c))
        counter+=1
    if klen % 64 != 0:
        Ha[time-1] = Ha[time-1][0:(klen - (64 * (klen // 64)))]
    result = ''
    for i in range(len(Ha)):
        result = result + Ha[i]
    return '0x'+result
def encrypt(p,a,b,Gx,Gy,Par,text,PBx,PBy,k,klen):
    C1x,C1y = mult(Gx,Gy,p,a,k)
    C1x,C1y = transTheSet(C1x,C1y,Par)
    C1 = '04' + C1x + C1y
    x2,y2 = mult(PBx,PBy,p,a,k)
    x2,y2 = transTheSet(x2,y2,Par)
    t = KDF(x2+y2,klen)
    C2 = hex(eval(t) ^ eval('0x'+text))[2:]
    C3 = Hash(x2+text+y2)
    print('0x'+C1+C2+C3)
def decrypt(p,a,b,Gx,Gy,Par,text,dB):
    ciphertext = text[2:]
    C1x = eval('0x'+ciphertext[0:Par//4])
    C1y = eval('0x'+ciphertext[Par//4:Par//2])
    C2 = ciphertext[Par//2:len(ciphertext)-64]
    klen = len(C2)
    x2,y2 = mult(C1x,C1y,p,a,dB)
    x2, y2 = transTheSet(x2, y2, Par)
    t = KDF(x2+y2,klen)
    plaintext = hex(eval(t) ^ eval('0x' + C2))[2:]
    print('0x'+plaintext)
def SM2(p,a,b,Gx,Gy,Par,op,text,klen):
    if op == 1:
        PBx, PBy = map(int, input().split())
        k = int(input())
        encrypt(p,a,b,Gx,Gy,Par,text,PBx,PBy,k,klen)
    else:
        dB = int(input())
        decrypt(p,a,b,Gx,Gy,Par,text,dB)
if __name__ == '__main__':
    p = int(input())
    a = int(input())
    b = int(input())
    Gx, Gy = map(int, input().split())
    Par = int(input())
    op = int(input())
    text =input()[2:]
    klen = len(text)
    SM2(p,a,b,Gx,Gy,Par,op,text,klen)