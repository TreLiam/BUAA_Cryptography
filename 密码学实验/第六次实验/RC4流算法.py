oneByte = pow(2,8)
halfByte = pow(2,4)
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
def change_2bits(num):
    c = ''
    a = [0,0]
    a[1] = TranstoChar(num % 16)
    a[0] = TranstoChar(num//16)
    c = a[0] + a[1]
    return c
def CharToInt(c,d):
    if c == '0':
        a = 0
    elif c == '1':
        a = 1
    elif c == '2':
        a = 2
    elif c == '3':
        a = 3
    elif c == '4':
        a = 4
    elif c == '5':
        a = 5
    elif c == '6':
        a = 6
    elif c == '7':
        a = 7
    elif c == '8':
        a = 8
    elif c == '9':
        a = 9
    elif c == 'a':
        a = 10
    elif c == 'b':
        a = 11
    elif c == 'c':
        a = 12
    elif c == 'd':
        a = 13
    elif c == 'e':
        a = 14
    else:
        a = 15
    if d == '0':
        b = 0
    elif d == '1':
        b = 1
    elif d == '2':
        b = 2
    elif d == '3':
        b = 3
    elif d == '4':
        b = 4
    elif d == '5':
        b = 5
    elif d == '6':
        b = 6
    elif d == '7':
        b = 7
    elif d == '8':
        b = 8
    elif d == '9':
        b = 9
    elif d == 'a':
        b = 10
    elif d == 'b':
        b = 11
    elif d == 'c':
        b = 12
    elif d == 'd':
        b = 13
    elif d == 'e':
        b = 14
    else:
        b = 15
    num = a * 16 + b
    return num
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
def KSA(key):
    #初始化S和T
    S = []
    T = []
    for i in range(256):
        S.append(i)
        T.append(key[i % len(key)])
    #S的初始置换
    j = 0
    for i in range(256):
        j = (j+S[i]+T[i]) % 256
        S[i],S[j] = swap(S[i],S[j])
    return S
def RC4(key,text):
    S = KSA(key)
    i = 0
    j = 0
    print('0x',end='')
    for m in range((len(text)-2)//2):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = swap(S[i], S[j])
        t = (S[i] + S[j]) % 256
        Ks = S[t]
        num = Ks ^ CharToInt(text[2+m*2],text[2+m*2+1])
        c = change_2bits(num)
        print(c[0]+c[1],end='')
if __name__ == '__main__':
    k = input()
    k = k.replace('\n', '')
    k = k.replace('\r', '')
    k = list(k)
    k.pop(0)
    k.pop(0)
    key = []
    for i in range(len(k)//2):
        a = TranstoNum(k[2*i])
        b = TranstoNum(k[2*i+1])
        num = 16*a+b
        key.append(num)
    s = input()
    s = s.replace('\n', '')
    s = s.replace('\r', '')
    RC4(key,s)
