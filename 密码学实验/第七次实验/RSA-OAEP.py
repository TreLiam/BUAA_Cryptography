import hashlib
def extend(s, k):
    lengh = len(s)
    while lengh <  2 * k:
        s = '0' + s
        lengh = len(s)
    return s
def Hash(res):
    if len(res) % 2 != 0:
        res = '0' + res
    sha = hashlib.sha1(bytearray.fromhex(res))
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
def decrypt(c,d,n):
    plaintext = fastMode(c,d,n)
    return plaintext
def RSA(e,n,M,op):
    if op == 1:
        ciphertext = encrypt(M,e,n)
        return ciphertext
    else :
        d = e
        plaintext = decrypt(M,d,n)
        return plaintext
def getDB(lhash,hLen,k,mLen,text):
    PS = ''
    for i in range(k - mLen - 2 * hLen -2):
        PS = PS + '00'
    DB = lhash + PS + '01' + text
    return DB
def MGF1(X,maskLen):
    if len(X) % 2 != 0:
        X = '0' + X
    T = ''
    C = X + '00000000'
    T = T + Hash(C)
    tLen = len(T)//2
    counter = 1
    if tLen == maskLen:
        return T
    else:
        while maskLen > tLen:
            mid = '00000000'
            C = hex(counter)
            C = C[2:]
            C = mid[0:8-len(C)]+C
            half = X + C
            T = T + Hash(half)
            tLen = len(T)//2
            counter+=1
        return T[0:2*maskLen]
def RSA_OAEP(op,k,e,N,text,L):
    if op == 1:
        Seed = input()
        Seed = Seed[2:]
        lLen = len(L)//2
        # 如果 L 的长度超出哈希函数的输入限制 （SHA-1 的限制是 pow(2,61) – 1 个八位组）
        if lLen >= pow(2,61) - 1:
            return 'Err'
        mLen = len(text)//2
        lhash = Hash(L)
        hLen = len(lhash)//2
        #填充Seed
        Seed = extend(Seed,hLen)
        #如果 mLen > k – 2hLen – 2，
        if mLen > k - 2*hLen - 2:
            return 'Err'
        else:
            DB = getDB(lhash,hLen,k,mLen,text)
            MGF_Seed = MGF1(Seed,k - hLen - 1)
            a = eval('0x' + DB)
            b = eval('0x' + MGF_Seed)
            maskedDB = hex(a ^ b)
            maskedDB = maskedDB[2:]
            maskedDB = extend(maskedDB,k - hLen - 1)
            MGF_DB = MGF1(maskedDB, hLen)
            c = eval('0x' + Seed)
            d = eval('0x' + MGF_DB)
            maskedSeed = hex(c^d)
            maskedSeed = maskedSeed[2:]
            maskedSeed = extend(maskedSeed,hLen)
            EM = '0x00'+maskedSeed+maskedDB
            M = eval(EM)
            res = hex(RSA(e,N,M,op))
            res = res[2:]
            res = '0x'+extend(res,k)
            return res
    else:
        lLen = len(L)//2
        # 如果 L 的长度超出哈希函数的输入限制 （SHA-1 的限制是 pow(2,61) – 1 个八位组）
        if lLen >= pow(2, 61) - 1:
            return 'Ree'
        mLen = len(text) // 2
        # 如果密文 C 的长度不是 k 个八位组
        if mLen != k:
            return 'Ree'
        lhash = Hash(L)
        hLen = len(lhash) // 2
        # 如果 k < 2hLen + 2
        if k < 2*hLen + 2:
            return 'Ree'
        M = eval('0x'+text)
        #“密文代表超出范围”（意思是 c ≥ n）
        if M >= N:
            return 'Ree'
        EM = hex(RSA(e,N,M,op))
        EM = EM[2:]
        if len(EM) > 2*(k-1):
            return 'Ree'
        EM = extend(EM,k-1)
        maskedSeed = EM[0:2*hLen]
        maskedDB = EM[2*hLen:]
        seedmask = MGF1(maskedDB, hLen)
        a = eval('0x'+maskedSeed)
        b = eval('0x'+seedmask)
        seed = hex(a^b)
        seed = seed[2:]
        seed = extend(seed,hLen)
        DBmask = MGF1(seed, k - hLen - 1)
        c = eval('0x' + maskedDB)
        d = eval('0x' + DBmask)
        DB = hex(c^d)
        DB = DB[2:]
        DB = extend(DB,k - hLen - 1)
        index = DB.find('01', 2 * hLen, len(DB))
        if index == -1:
            return 'Ree'
        res = '0x' + DB[index + 2:]
        return hex(eval(res))
if __name__ == '__main__':
    op = int(input())
    k = int(input())
    e = eval(input())
    N = eval(input())
    text = input()
    text = text[2:]
    L = input()
    L = L[2:]
    print(RSA_OAEP(op,k,e,N,text,L))
