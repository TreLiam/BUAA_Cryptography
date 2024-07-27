def add(a,b):
    return  a^b
def mult(a,b):
    result = 0
    while b>0:
        if b%2 == 1:
            result ^= a
        a = gmul(a,0x11b)
        b >>= 1
    return result
def gmul(a,poly):
    a <<= 1
    if a&0x100 == 0x100:
        a ^= poly
    return a & 0xff
def div(a,b):
    q = 0
    while a.bit_length() >= b.bit_length():
        rec = a.bit_length()- b.bit_length()
        a ^= (b << rec)
        q ^= (1 << rec)
    return q,a
def exEuclid(a,b):
    if b == 0:
        return a, 1, 0
    else:
        q,r = div(a,b)
        GCD,xtmp,ytmp = exEuclid(b,r)
        x = ytmp
        y = xtmp ^ mult(ytmp,q)
        return GCD,x,y
def trans(c):
    if c == '0':
        ans = 0
    elif c == '1':
        ans = 1
    elif c == '2':
        ans = 2
    elif c == '3':
        ans = 3
    elif c == '4':
        ans = 4
    elif c == '5':
        ans = 5
    elif c == '6':
        ans = 6
    elif c == '7':
        ans = 7
    elif c == '8':
        ans = 8
    elif c == '9':
        ans = 9
    elif c == 'a':
        ans = 10
    elif c == 'b':
        ans = 11
    elif c == 'c':
        ans = 12
    elif c == 'd':
        ans = 13
    elif c == 'e':
        ans = 14
    else:
        ans = 15
    return ans

def first():
    num = 0
    result = []
    for i in range(16):
        result.append([])
        for j in range(16):
            result[i].append(num)
            num += 1
    return result
def second(s):
    result = []
    for i in range(16):
        result.append([])
        for j in range(16):
            GCD, x, y = exEuclid(s[i][j], 0x11b)
            result[i].append(x)
    return result
def third(s):
    result = []
    b = [0,0,0,0,0,0,0,0]
    d = [0,0,0,0,0,0,0,0]
    c = [0,1,1,0,0,0,1,1]
    for i in range(16):
        result.append([])
        for j in range(16):
            num = s[i][j]
            for k in range(8):
                b[k] = 0
                d[k] = 0
            for k in range(8):
                b[k] = num%2
                num = num//2
            for k in range(8):
                d[7-k] = ((((b[k]^b[(k+4)%8])^b[(k+5)%8])^b[(k+6)%8])^b[(k+7)%8])^c[7-k]
            sum = d[7] + d[6]*2 + d[5]*4 + d[4]*8 + d[3]*16 + d[2]*32 + d[1]*64 +d[0]*128
            result[i].append(sum)
    return result

def fourth(s):
    result = []
    for i in range(16):
        result.append([])
        for j in range(16):
            result[i].append(0)
    for i in range(16):
        for j in range(16):
            num = list(hex(s[i][j]))
            if len(num) == 3:
                num.insert(2,'0')
            a = trans(num[2])
            b = trans(num[3])
            result[a][b] = 16*i +j
    return result





if __name__ == '__main__':
    s = []
    s = first()
    for i in range(16):
        for j in range(16):
            p = s[i][j]
            print('0x%02x' %p,end = ' ')
        print('\n')
    s = second(s)
    for i in range(16):
        for j in range(16):
            p = s[i][j]
            print('0x%02x' %p,end = ' ')
        print('\n')
    s = third(s)
    for i in range(16):
        for j in range(16):
            p = s[i][j]
            print('0x%02x' %p, end=' ')
        print('\n')
    s = fourth(s)
    for i in range(16):
        for j in range(16):
            p = s[i][j]
            print('0x%02x' % p, end=' ')
        print('\n')