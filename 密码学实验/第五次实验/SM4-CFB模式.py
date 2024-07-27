import sys
Sbox = [[0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05],
[0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99],
[0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62],
[0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6],
[0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8],
[0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35],
[0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87],
[0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e],
[0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1],
[0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3],
[0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f],
[0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51],
[0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8],
[0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0],
[0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84],
[0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]]
CK=[
0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269, 0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249, 0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229, 0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209, 0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279]
FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc]
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
def list_move_left(B,a):
    num1 = pow(2,32-a)
    num2 = pow(2,a)
    midr = B % num1
    midl = B // num1
    new = midr*num2 + midl
    return new
def TranstoNum(c):
    if c == '0':
        result = 0
    elif c == '1':
        result = 1
    elif c == '2':
        result = 2
    elif c == '3':
        result = 3
    elif c == '4':
        result = 4
    elif c == '5':
        result = 5
    elif c == '6':
        result = 6
    elif c == '7':
        result = 7
    elif c == '8':
        result = 8
    elif c == '9':
        result = 9
    elif c == 'a':
        result = 10
    elif c == 'b':
        result = 11
    elif c == 'c':
        result = 12
    elif c == 'd':
        result = 13
    elif c == 'e':
        result = 14
    else:
        result = 15
    return result
def TranstoChar(num):
    if num == 0:
        c = '0'
    elif num == 1:
        c = '1'
    elif num == 2:
        c = '2'
    elif num == 3:
        c = '3'
    elif num == 4:
        c = '4'
    elif num == 5:
        c = '5'
    elif num == 6:
        c = '6'
    elif num == 7:
        c = '7'
    elif num == 8:
        c = '8'
    elif num == 9:
        c = '9'
    elif num == 10:
        c = 'a'
    elif num == 11:
        c = 'b'
    elif num == 12:
        c = 'c'
    elif num == 13:
        c = 'd'
    elif num == 14:
        c = 'e'
    else:
        c = 'f'
    return c
def ChangetoNum(s):
    c = s[0]
    sum = 0
    gamble = 1
    num = []
    for i in range(len(c)):
        num.append(TranstoNum(c[i]))

    for i in range(len(c)-1,-1,-1):
        sum = sum + gamble*num[i]
        gamble *=16
    return sum
def ChangetoChar(num):
    a = [0,0,0,0,0,0,0,0]
    for i in range(8):
        a[7-i] = TranstoChar(num%16)
        num = num//16
    c = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7]
    return c
def ChangetoString(number,num):
    a = []
    for i in range(num*2):
        a.append(0)
    c = ''
    for i in range(num*2):
        a[num*2-1-i] = TranstoChar(number % 16)
        number = number//16
    for i in range(num*2):
        c = c + a[i]
    return c
def change_2bits(num):
    a = [0,0]
    a[1] = TranstoChar(num % 16)
    a[0] = TranstoChar(num//16)
    c = a[0] + a[1]
    return c
def S(W):
    W = ChangetoChar(W)
    result1 = 0
    bet = pow(16,6)
    for i in range(4):
        a = TranstoNum(W[2*i])
        b = TranstoNum(W[2*i+1])
        result1 = result1 + bet*Sbox[a][b]
        bet //= 256
    return result1
def L(B):
    result = B ^ (list_move_left(B,2)) ^ (list_move_left(B,10)) ^ (list_move_left(B,18)) ^ (list_move_left(B,24))
    return result
def T(B):
    return L(S(B))
def anotherL(B):
    result = B ^ (list_move_left(B,13)) ^ (list_move_left(B,23))
    return result
def anotherT(B):
    return anotherL(S(B))
def generateKey(prekey):
    key = []
    roundKey = []
    for i in range(4):
        key.append(FK[i]^ChangetoNum(prekey[i]))
    for i in range(32):
        keylist = key[i] ^ anotherT(key[i+1] ^ key[i+2] ^ key[i+3] ^ CK[i])
        key.append(keylist)
        roundKey.append(keylist)
    return roundKey
def encrypt(time,plaintext,roundKey):
    for j in range(time):
        X = plaintext
        for i in range(32):
            X.append(X[i] ^ T(X[i+1] ^ X[i+2] ^ X[i+3] ^ roundKey[i]))
    ciphertext = [X[35],X[34],X[33],X[32]]
    return ciphertext
def decrypt(time,ciphertext,roundKey):
    text = []
    for i in range(4):
        text.append(ChangetoNum(ciphertext[i]))
    for j in range(time):
        X = text
        for i in range(32):
            X.append(X[i] ^ T(X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ roundKey[31 - i]))
        text = [X[35], X[34], X[33], X[32]]
    plaintext = text
    return plaintext
def SM4_CFB(text,k,op,VI,num,leave):
    t1 = pow(16,24)
    t2 = pow(16,16)
    t3 = pow(16,8)
    t4 = pow(16,32-2*num)
    t5 = pow(16,2*num)
    article = ''
    roundKey = generateKey(k)
    shift_counter =[ChangetoNum([VI[0] + VI[1] + VI[2] + VI[3] + VI[4] + VI[5] +VI[6] + VI[7]]),
                    ChangetoNum([VI[8] + VI[9] + VI[10] + VI[11] + VI[12] + VI[13] + VI[14] + VI[15]]),
                    ChangetoNum([VI[16] + VI[17] + VI[18] + VI[19] + VI[20] + VI[21] + VI[22] + VI[23]]),
                    ChangetoNum([VI[24] + VI[25] + VI[26] + VI[27] + VI[28] + VI[29] + VI[30] + VI[31]])]#转换成进行加密的结构
    thecounter = t1*shift_counter[0] + t2*shift_counter[1] + t3*shift_counter[2] + shift_counter[3]
    if op == 1:
            for i in range(len(text)):
                halftext = encrypt(1,shift_counter,roundKey) #加密移位储存器
                midway = t1*halftext[0] + t2*halftext[1] + t3*halftext[2] + halftext[3]
                xortext = midway // t4 #截取n位
                ciphertext = xortext ^ text[i] #进行异或
                article = article + ChangetoString(ciphertext,num) #录入输出
                thecounter = (thecounter % t4)*t5 + ciphertext#进行左移
                a = thecounter // t1
                b = (thecounter % t1)//t2
                c = ((thecounter % t1)%t2)//t3
                d = thecounter % t3
                shift_counter = [a,b,c,d]
    else:
        for i in range(len(text)):
            halftext = encrypt(1, shift_counter, roundKey)  # 加密移位储存器
            midway = t1 * halftext[0] + t2 * halftext[1] + t3 * halftext[2] + halftext[3]
            xortext = midway // t4  # 截取n位
            ciphertext = xortext ^ text[i]  # 进行异或
            article = article + ChangetoString(ciphertext, num)  # 录入输出
            thecounter = (thecounter % t4) * t5 + text[i]  # 进行左移
            a = thecounter // t1
            b = (thecounter % t1) // t2
            c = ((thecounter % t1) % t2) // t3
            d = thecounter % t3
            shift_counter = [a, b, c, d]
        # 打印
    for i in range(0, len(article) - 2 * leave, 2):
        print('0x' + article[i] + article[i + 1], end=' ')
        if (i + 2) % 32 == 0:
            print()
if __name__ == '__main__':
    n = int(input())
    k = input()
    k = list(k)
    k.pop(0)
    k.pop(0)
    k = [[k[0] + k[1] + k[2] + k[3] + k[4] + k[5] + k[6] + k[7]],
         [k[8] + k[9] + k[10] + k[11] + k[12] + k[13] + k[14] + k[15]],
         [k[16] + k[17] + k[18] + k[19] + k[20] + k[21] + k[22] + k[23]],
         [k[24] + k[25] + k[26] + k[27] + k[28] + k[29] + k[30] + k[31]]]
    VI = input()
    VI = VI.replace('\n', '')
    VI = VI.replace('\r', '')
    VI = list(VI)
    VI.pop(0)
    VI.pop(0)
    op = int(input())
    name = sys.stdin.read()
    name = name.replace('\n', '')
    name = name.replace('\r', '')
    s = list(name)
    text = []
    for i in range(len(s) // 5):
        text.append(s[5 * i + 2] + s[5 * i + 3])
    if len(text) % n == 0:
        leave = 0
    else:
        leave = n - len(text)%n
    c = change_2bits(leave)
    for i in range(leave):
        text.append(c)
    realtext = []
    for i in range(0,len(text),n):
        c = ''
        for j in range(n):
            c = c + text[i + j]
        realtext.append(ChangetoNum([c]))
    SM4_CFB(realtext,k,op,VI,n,leave)