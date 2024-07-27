import hashlib
import math
def creat_Link(e):
    e_bin = bin(e)[2:]
    B = []
    max = 0
    sum1 = 0
    sum0 = 0
    for i in range(len(e_bin)):
        if i == len(e_bin)-1:
            if e_bin[i] != e_bin[i-1]:
                flag = 0
            else:
                flag = 1
            if e_bin[i] == '1':
                sum1 += 1
                if flag == 0:
                    B.append(sum0)
                    B.append(sum1)
                else:
                    B.append(sum1)
            else:
                sum0 += 1
                if flag == 0:
                    B.append(sum1)
                    B.append(sum0)
                else:
                    B.append(sum0)
            if sum1 != 0:
                if max < sum1:
                    max = sum1
        else:
            if e_bin[i] == '1':
                if sum0 != 0:
                    B.append(sum0)
                    sum0 = 0
                sum1 += 1
            else:
                if max < sum1:
                    max = sum1
                if sum1 != 0:
                    B.append(sum1)
                    sum1 = 0
                sum0 += 1
    D = []
    for i in range(1,max+1):
        num = pow(2,i)
        D.append(num-1)
        if num != 2:
            D.append(num-2)
    number = 0
    for i in range(len(B)):
        if i == 0:
            number = pow(2,B[i]) - 1
            D.append(number)
        elif i % 2 == 0:
            add = pow(2,B[i]) - 1
            for j in range(B[i]):
                number *= 2
                D.append(number)
            number += add
            D.append(number)
        else:
            for j in range(B[i]):
                number *= 2
                D.append(number)
    finalD = list(set(D))
    finalD.sort()
    return finalD
def fast_pow(M,e,N):
    D = creat_Link(e)
    powers = [M]
    for k in range(1,len(D)):
        if D[k] % 2 == 0:
            sp = D.index(D[k] // 2)
            powers.append((powers[sp] * powers[sp]) % N)
        else:
            i = k - 1
            j = D.index(D[k] - D[i])
            powers.append((powers[i] * powers[j]) % N)
    return(powers[len(D)-1])
def mont(base,exp,p):
    res=1
    while exp>0:
        if exp%2==1:
            res=(res*base)%p
        exp=exp>>1
        base=(base*base)%p

    return res
def hash(m: bytes) -> str:
    return hashlib.sha1(m).hexdigest()
def MGF(mgfseed, masklen, hlen):
    if masklen > 2**32 * hlen:
        print("mask is too long")
        return -1
    T = b''
    X = bytearray.fromhex(mgfseed)
    for counter in range(math.ceil(masklen // hlen) - 1):
        tmp = X + bytearray.fromhex('%08x' % counter)
        T += hash(tmp).encode()
    return T[:masklen]
def encode(M: str, salt: str, embits: int) -> str:
    slen = 20
    emlen = math.ceil(embits/8)
    hlen = 20

    mhash = hash(M.encode())
    M1 = '0000000000000000' + mhash + salt
    H = hash(bytes.fromhex(M1))
    DB = '00' * (emlen - slen - hlen - 2) + '01' + salt
    dbmask = MGF(H, 2*(emlen-hlen-1), hlen)
    maskedDB = list(bin(int(DB,16 ) ^ int(dbmask, 16))[2:].zfill(8*(emlen-hlen-1)))
    for i in range((8*emlen-embits)):
        maskedDB[i] = '0'
    maskedDB = hex(int(''.join(maskedDB), 2))[2:].zfill(2*(emlen-hlen-1))
    EM = maskedDB + H + 'bc'
    return EM
def sign(M, n, embits, d, salt):
    EM = encode(M, salt, embits)
    m = int(EM, 16)
    emlen = math.ceil(embits / 8)
    return hex(int(mont(m, d, n)))[2:].zfill(emlen*2)
def verify(M, n, embits, e, s):
    emlen = math.ceil(embits/8)
    hlen = 20
    slen = 20
    EM = hex(mont(int(s, 16), e, n))[2:].zfill(emlen*2)
    mhash = hash(M.encode())
    if emlen < hlen + slen + 2:
        return False
    if EM[-2]+EM[-1] != 'bc':
        return False
    maskedDB = EM[:2*(emlen-hlen-1)]
    H = EM[2*(emlen-hlen-1):2*(emlen-hlen-1)+2*hlen]
    if bin(int(maskedDB, 16))[2:].zfill(8*(emlen-hlen-1))[:8*emlen-embits] != (8*emlen-embits)*'0':
        return False
    dbmask = MGF(H, (emlen-hlen-1)*2, hlen)
    DB = list(bin(int(dbmask, 16) ^ int(maskedDB, 16))[2:].zfill((emlen-hlen-1)*8))
    for i in range((8 * emlen - embits)):
        DB[i] = '0'
    DB = hex(int(''.join(DB), 2))[2:].zfill(2 * (emlen - hlen - 1))
    padding2 = '00' * (emlen - slen - hlen - 2) + '01'
    if DB[:2*(emlen-hlen-slen-1)] != padding2:
        return False
    salt = DB[len(DB)-2*slen:]
    M1 = '0000000000000000' + mhash + salt
    H1 = hash(bytes.fromhex(M1))
    return H1 == H
if __name__ == '__main__':
    M = input()
    n = int(input())
    embits = int(input())
    mode = input()
    if mode == 'Sign':
        d = int(input())
        salt = input()
        print(sign(M, n, embits, d, salt))
    elif mode == 'Vrfy':
        e = int(input())
        s = input()
        print(verify(M, n, embits, e, s))
