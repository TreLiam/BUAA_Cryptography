import math
from hashlib import sha1
def format2hex(num, n):
    if(n == -1):
        n = len(hex(num)) - 2
    return hex(num)[2:].rjust(n, '0')
def Hash(res):
    if len(res) % 2 != 0:
        res = '0' + res
    sha = sha1(bytearray.fromhex(res))
    encrypts = sha.hexdigest()
    return encrypts
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
def fastMode(base,expo,p):
    ans = 1
    while expo > 0:
        a = expo % 2
        expo = expo >> 1
        if a == 1:
            ans = (ans * base) % p
        base = (base * base) % p
    return ans
def Sign_RSA_PSS(M,n,emBits,Mode):
    hLen = 20
    sLen = 20
    emLen = emBits // 8 if emBits % 8 == 0 else emBits // 8 + 1
    mHash = sha1(M.encode('utf-8')).hexdigest()
    if Mode == 'Sign':
        d = int(input())
        salt = input()
        message = '0000000000000000' + mHash + salt
        H = Hash(message)
        the_fill = ''
        for i in range(emLen - hLen - sLen - 2):
            the_fill = the_fill + '00'
        the_fill = the_fill + '01'
        DB = the_fill + salt
        dbMask = MGF1(H,emLen - hLen - 1)
        maskedDB = bin(eval('0x' + DB) ^ eval('0x' + dbMask))[2:].zfill(8 * (emLen - hLen - 1))
        maskedDB = list(maskedDB)
        for i in range(8 * emLen - emBits):
            maskedDB[i] = '0'
        maskedDB =''.join(maskedDB)
        maskedDB = hex(eval('0b'+maskedDB))[2:].zfill(2 * (emLen - hLen - 1))
        EM = maskedDB + H + 'bc'
        m = eval('0x'+EM)
        s =  fastMode(m,d,n)
        S = hex(s)[2:].zfill(256)
        print(S)
    else:
        e = int(input())
        S = input()
        m = fastMode(eval('0x'+S),e,n)
        EM = hex(m)[2:].zfill(2*emLen)
        if emLen < hLen + sLen + 2:
            print('False')
        elif (EM[len(EM) - 2]!= 'b') &(EM[len(EM) - 1] != 'c'):
            print('False')
        else:
            maskedDB = EM[0:2*(emLen - hLen - 1)]
            H = EM[2*(emLen - hLen - 1):2 *(emLen - 1)]
            mid = bin(eval('0x'+maskedDB))[2:].zfill(8 * (emLen - hLen - 1))
            flag = 0
            for i in range(8*emLen - emBits):
                if mid[i] != '0':
                    flag = 1
                    break
            if flag == 1:
                print('False')
            else:
                dbMask = MGF1(H,emLen - hLen - 1)
                DB = bin(eval('0x'+dbMask) ^ eval('0x' + maskedDB))[2:].zfill(8 * (emLen - hLen - 1))
                DB = list(DB)
                for i in range(8 * emLen - emBits):
                    DB[i] = '0'
                DB = ''.join(DB)
                DB = hex(eval('0b' + DB))[2:].zfill(2 * (emLen - hLen - 1))
                the_fill = ''
                for i in range(emLen - hLen - sLen - 2):
                    the_fill = the_fill + '00'
                the_fill = the_fill + '01'
                flag = 0
                for i in range(2 * (emLen - hLen - sLen -1)):
                    if the_fill[i] != DB[i]:
                        flag = 1
                        break
                if flag == 1:
                    print('False')
                else:
                    flag = 0
                    salt = DB[len(DB) - 2 * sLen:len(DB)]
                    _M = '0000000000000000' + mHash + salt
                    _H = Hash(_M)
                    for i in range(len(H)):
                        if H[i] != _H[i]:
                            flag = 1
                            break
                    if flag == 1:
                        print('False')
                    else:
                        print('True')

if __name__ == '__main__':
    M = input()
    M = M.replace('\n', '')
    M = M.replace('\r', '')
    n = int(input())
    emBits = int(input())
    Mode = input()
    Sign_RSA_PSS(M,n,emBits,Mode)