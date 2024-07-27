IP = [58, 50, 42, 34, 26, 18, 10,  2,
        60, 52, 44, 36, 28, 20, 12,  4,
        62, 54, 46, 38, 30, 22, 14,  6,
        64, 56, 48, 40, 32, 24, 16,  8,
        57, 49, 41, 33, 25, 17,  9,  1,
        59, 51, 43, 35, 27, 19, 11,  3,
        61, 53, 45, 37, 29, 21, 13,  5,
        63, 55, 47, 39, 31, 23, 15,  7]
IPverse = [40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,
            38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,
            36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,
            34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
keysub1 = [57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]
keysub2 = [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
keyext = [32,  1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
 8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,  1]
keyleft = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
           ]
PBox = [16,  7, 20, 21, 29, 12, 28, 17,  1, 15, 23, 26,  5, 18, 31, 10,
 2,  8, 24, 14, 32, 27,  3,  9, 19, 13, 30,  6, 22, 11,  4, 25
]
SB1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
]
SB2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
]
SB3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
SB4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
]
SB5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
]
SB6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
]
SB7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
]
SB8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
SB = [SB1,SB2,SB3,SB4,SB5,SB6,SB7,SB8]

def test(l):
    li = '0x'
    for i in range(0,len(l),4):
        sum = l[i+3] + l[i+2] * 2 + l[i+1] * 4 + l[i] * 8
        if sum == 0:
            li = li +'0'
        elif sum == 1:
            li = li + '1'
        elif sum == 2:
            li = li + '2'
        elif sum == 3:
            li = li + '3'
        elif sum == 4:
            li = li + '4'
        elif sum == 5:
            li = li + '5'
        elif sum == 6:
            li = li + '6'
        elif sum == 7:
            li = li + '7'
        elif sum == 8:
            li = li + '8'
        elif sum == 9:
            li = li + '9'
        elif sum == 10:
            li = li + 'a'
        elif sum == 11:
            li = li + 'b'
        elif sum == 12:
            li = li + 'c'
        elif sum == 13:
            li = li + 'd'
        elif sum == 14:
            li = li + 'e'
        else:
            li = li + 'f'
    print(li)

def XtoB(c):
    if c == '0':
        return [0,0,0,0]
    elif c == '1':
        return [0,0,0,1]
    elif c == '2':
        return [0, 0, 1, 0]
    elif c == '3':
        return [0, 0, 1, 1]
    elif c == '4':
        return [0, 1, 0, 0]
    elif c == '5':
        return [0, 1, 0, 1]
    elif c == '6':
        return [0, 1, 1, 0]
    elif c == '7':
        return [0, 1, 1, 1]
    elif c == '8':
        return [1, 0, 0, 0]
    elif c == '9':
        return [1, 0, 0, 1]
    elif c == 'a':
        return [1, 0, 1, 0]
    elif c == 'b':
        return [1, 0, 1, 1]
    elif c == 'c':
        return [1, 1, 0, 0]
    elif c == 'd':
        return [1, 1, 0, 1]
    elif c == 'e':
        return [1, 1, 1, 0]
    else:
        return [1, 1, 1, 1]

def XtoAnotherB(c):
    if c == 0:
        return [0,0,0,0]
    elif c == 1:
        return [0,0,0,1]
    elif c == 2:
        return [0, 0, 1, 0]
    elif c == 3:
        return [0, 0, 1, 1]
    elif c == 4:
        return [0, 1, 0, 0]
    elif c == 5:
        return [0, 1, 0, 1]
    elif c == 6:
        return [0, 1, 1, 0]
    elif c == 7:
        return [0, 1, 1, 1]
    elif c == 8:
        return [1, 0, 0, 0]
    elif c == 9:
        return [1, 0, 0, 1]
    elif c == 10:
        return [1, 0, 1, 0]
    elif c == 11:
        return [1, 0, 1, 1]
    elif c == 12:
        return [1, 1, 0, 0]
    elif c == 13:
        return [1, 1, 0, 1]
    elif c == 14:
        return [1, 1, 1, 0]
    else:
        return [1, 1, 1, 1]


def trans(k):
    k.pop(0)
    k.pop(0)
    ans = []
    for i in range(len(k)):
        ans = ans + XtoB(k[i])
    return ans

def moveNum(lizz,num):
    ex = []
    for i in range(num):
        ex.append(lizz[i])
    for i in range(num,len(lizz)):
        lizz[i-num] = lizz[i]
    ex.reverse()
    for i in range(num):
        lizz[len(lizz)-i-1] = ex[i]
    return lizz

def generatekey(key):
    key = trans(key)
    keylist = []
    for i in range(56):
        keylist.append(key[keysub1[i]-1]) #置换选择1
    D = []
    C = []
    for i in range(28):
        C.append(keylist[i])
        D.append(keylist[28+i])
    roundkey = []
    for i in range(16):
        roundkey.append([])
        C = moveNum(C,keyleft[i])
        D = moveNum(D,keyleft[i])
        anotherkey = C+D
        for j in range(48):
            roundkey[i].append(anotherkey[keysub2[j]-1])
    return roundkey

def swap(plaintext):
    message = []
    for i in range(len(plaintext)):
        message.append(plaintext[IP[i]-1])
    return message

def Invswap(afterF):
    ciphertext = []
    for i in range(len(afterF)):
        ciphertext.append(afterF[IPverse[i]-1])
    return ciphertext

def extend(right):
    result = []
    for i in range(48):
        result.append(right[keyext[i]-1])
    #test(result)
    return result

def sbox(half):
    result = []
    ans = []
    for i in range(8):
        a = half[6*i]*2+half[6*i+5]
        b = half[6*i+1]*8+half[6*i+2]*4+half[6*i+3]*2+half[6*i+4]
        result.append(SB[i][a*16+b])
    for i in range(len(result)):
        ans = ans + XtoAnotherB(result[i])
    return ans

def pbox(halfway):
    result = []
    for i in range(len(halfway)):
        result.append(halfway[PBox[i]-1])
    return result

def f(m,n):
    mess  = xor(extend(m),n)
    messa = sbox(mess)
    messag = pbox(messa)
    return messag

def xor(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i]^b[i])
    return result


def encrypt(time,plaintext,roundKey):
    plaintext = trans(plaintext)
    for k in range(time):
        message = swap(plaintext)
        L = []
        R = []
        for i in range(17):
            L.append([])
            R.append([])
        for i in range(32):
            L[0].append(message[i])
            R[0].append(message[i+32])
        for i in range(1,17):
            L[i] = R[i-1]
            R[i] = xor(L[i-1],f(R[i-1],roundKey[i-1]))
        afterF = R[16]+L[16]
        plaintext = Invswap(afterF)
    return plaintext

def decrypt(time,ciphertext,roundKey):
    ciphertext = trans(ciphertext)
    for k in range(time):
        message = swap(ciphertext)
        L = []
        R = []
        for i in range(18):
            L.append([])
            R.append([])
        for i in range(32):
            R[16].append(message[i])
            L[16].append(message[i + 32])
        for i in range(16, 0,-1):
            L[i-1] =xor(R[i], f(L[i], roundKey[i - 1]))
            R[i-1] = L[i]
            # test(L[i]+R[i])
        afterF = L[0] + R[0]
        ciphertext = Invswap(afterF)
    return ciphertext


def DES(t,s,k,op):
    if op == 1:
        test(encrypt(t,s,generatekey(k)))
    else:
        test(decrypt(t,s,generatekey(k)))


if __name__ == '__main__':
    t = int(input())
    s = input()
    s = s.replace('\n', '')
    s = s.replace('\r', '')
    s = list(s)
    k = input()
    k = k.replace('\n', '')
    k = k.replace('\r', '')
    k = list(k)
    op = int(input())
    DES(t,s,k,op)