import hashlib
import math
import gmpy2
# from pycallgraph import Config
# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput

def MGF(x, maskLen):
    if len(x) % 2 != 0:
        x = '0' + x

    T = bytearray(b'')
    X = bytearray.fromhex(x)

    counter = 0
    temp = X + bytearray.fromhex('00000000')
    T = T + bytearray.fromhex(hashlib.sha1(temp).hexdigest())
    HMlen = len(T.hex()) // 2
    counter += 1

    if maskLen == HMlen:
        return T.hex()
    else:
        tLen = len(T) // 2
        while maskLen > tLen:
            tmp = X + bytearray.fromhex('%08x' % counter)
            T = T + bytearray.fromhex(hashlib.sha1(tmp).hexdigest())
            tLen = len(T.hex()) // 2
            counter += 1
        return T.hex()[:2 * maskLen]


# res_len是16进制长度
def xor(X, Y, res_len):
    a = int(X, 16)
    b = int(Y, 16)
    temp = a ^ b
    res = hex(temp)[2:]

    temp_len = len(res)
    # 对异或结果进行填充，使得长度为res_len
    while temp_len < res_len:
        res = '0' + res
        temp_len = len(res)
    return res


def Sign(mes: str, salt: str, emlen: int, emBits, hlen=20, slen=20):
    mhash = hashlib.sha1(mes.encode()).hexdigest()
    padding1 = "0000000000000000"
    M_bar = padding1 + mhash + salt
    H = hashlib.sha1(bytes.fromhex(M_bar)).hexdigest()
    padding2 = "00" * (emlen - slen - hlen - 2) + "01"
    DB = padding2 + salt
    dbMask = MGF(H, emlen - hlen - 1)
    if len(DB) > len(dbMask):
        resLen = len(DB)
    else:
        resLen = len(dbMask)
    maskDB = xor(DB, dbMask, resLen)
    temp = "0" * ((8 * emlen - emBits) // 4)
    maskDB = temp + maskDB[(8 * emlen - emBits) // 4:]
    EM = maskDB + H + "bc"
    return EM


def Vrfy(S: str, e, n, mes: str, emBits, hlen=20, slen=20):
    S = "0x" + S
    s = gmpy2.mpz(S)
    m = gmpy2.powmod(s, e, n)
    EM = hex(m)[2:]


    emlen = math.ceil(emBits / 8)
    while len(EM) < 2 * emlen:
        EM = "0" + EM

    mhash = hashlib.sha1(mes.encode()).hexdigest()
    # if EM[-2:] != "bc":
    #     return "False"
    maskedDB = EM[:(emlen - hlen - 1) * 2]
    H = EM[(emlen - hlen - 1) * 2:(emlen - hlen - 1) * 2 + 2 * hlen]
    # if maskedDB[:(8 * emlen - emBits) // 4] != '0' * ((8 * emlen - emBits) // 4):
    #     return "False"
    dbMask = MGF(H, emlen - hlen - 1)
    # resLen = 0
    # if len(maskedDB) > len(dbMask):
    #     resLen = len(maskedDB)
    # else:
    #     resLen = len(dbMask)
    DB = xor(maskedDB, dbMask, len(dbMask))
    # temp 是二进制
    temp = "0" * (8 * emlen - emBits)
    DB_bin_str = bin(int(DB, 16))[2:]
    DB_bin_str=temp+DB_bin_str[8 * emlen - emBits:]

    # DB = temp + DB[(8 * emlen - emBits) // 4:]
    padding1 = "0000000000000000"
    # padding2 = "00" * (emlen - slen - hlen - 2) + "01"
    # if DB[:2 * (emlen - hlen - slen - 1)] != padding2:
    #     return "False"
    salt_bin = DB_bin_str[-8 * slen:]
    salt=hex(int(salt_bin,2))[2:]
    while len(salt)<2*slen:
        salt="0"+salt
    M_bar = padding1 + mhash + salt
    H_bar = hashlib.sha1(bytes.fromhex(M_bar)).hexdigest()
    if H == H_bar:
        return "True"
    else:
        return "False"


def RSAmain():
    mes = input()

    n = int(input())
    emBits = int(input())
    emlen = math.ceil(emBits / 8)
    Mode = input()
    if Mode == "Sign":
        d = int(input())
        salt = input()
        EM = "0x" + Sign(mes, salt, emlen, emBits)
        EM = gmpy2.mpz(EM)
        s = gmpy2.powmod(EM, d, n)
        s = hex(s)[2:]
        print(s)
    else:
        e = int(input())
        S = input()
        # print("True")
        print(Vrfy(S, e, n, mes, emBits))


if __name__ == '__main__':
    RSAmain()


