#coding=UTF-8
K = [0x5a827999,0x6ed9eba1,0x8f1bbcdc,0xca62c1d6]
def pad(plaintext):
    text = int.from_bytes(plaintext, "big")
    text = bin(text)[2:]
    while len(text) % 8 != 0:
        text = "0" + text
    tlen = len(text)
    b = tlen % 512
    if b == 448:
        k = 512
    elif b < 448:
        k = 448 - b
    else:
        k = 960 - b
    padding = text + "1" + (k - 1) * "0" + bin(tlen)[2:].zfill(64)
    return padding
def cls(num,sit):
    div = int(pow(2,32-sit))
    mult = int(pow(2,sit))
    a = num % div
    b = num // div
    result = a * mult + b
    return result
def extend(M):
    W = []
    for i in range(16):
        W.append('0b'+M[i*32:(i+1)*32])
    for i in range(16,80):
        mid = cls(eval(W[i-16]) ^ eval(W[i-14]) ^ eval(W[i-8]) ^ eval(W[i-3]),1)
        result = bin(mid)[2:].zfill(32)
        W.append('0b'+result)
    return W
def f(b,c,d,i):
    if (i>=0) & (i<20):
        result = (b & c) | ((~b)&d)
    elif (i>=20) & (i<40):
        result = b ^ c ^d
    elif (i>=40) & (i<60):
        result = (b&c) | (b&d) | (c&d)
    else:
        result = b ^ c ^ d
    return result
def round(W,h):
    div = int(pow(2, 32))
    a,b,c,d,e = h
    for i in range(80):
        if (i>=0) & (i<20):
            k = K[0]
        elif (i >= 20) & (i < 40):
            k = K[1]
        elif (i >= 40) & (i < 60):
            k = K[2]
        else:
            k = K[3]
        temp = (cls(a,5) + f(b,c,d,i) + e + eval(W[i]) + k) % div
        e = d
        d = c
        c = cls(b,30)
        b = a
        a = temp
    result = [(h[0] + a) % div,(h[1] + b) % div,(h[2] + c) % div,(h[3] + d) % div,(h[4] + e) % div]
    return result
def Hash(text):
    h = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]
    for i in range(len(text)//512):
        M = text[512*i:512*(i+1)]
        h = round(extend(M),h)
    print(hex(h[0])[2:].zfill(8)+hex(h[1])[2:].zfill(8)+hex(h[2])[2:].zfill(8)+hex(h[3])[2:].zfill(8)+hex(h[4])[2:].zfill(8))
if __name__ == '__main__':
    M = input()
    M = M.replace('\n', '')
    M = M.replace('\r','')
    message = M.encode("UTF-8")
    EM = pad(message)
    Hash(EM)