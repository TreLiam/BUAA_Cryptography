S = [['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],
['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],
['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],
['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],
['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],
['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],
['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],
['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],
['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],
['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],
['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],
['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],
['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],
['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],
['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']]
InvS = [['52','09','6a','d5','30','36','a5','38','bf','40','a3','9e','81','f3','d7','fb'],
['7c','e3','39','82','9b','2f','ff','87','34','8e','43','44','c4','de','e9','cb'],
['54','7b','94','32','a6','c2','23','3d','ee','4c','95','0b','42','fa','c3','4e'],
['08','2e','a1','66','28','d9','24','b2','76','5b','a2','49','6d','8b','d1','25'],
['72','f8','f6','64','86','68','98','16','d4','a4','5c','cc','5d','65','b6','92'],
['6c','70','48','50','fd','ed','b9','da','5e','15','46','57','a7','8d','9d','84'],
['90','d8','ab','00','8c','bc','d3','0a','f7','e4','58','05','b8','b3','45','06'],
['d0','2c','1e','8f','ca','3f','0f','02','c1','af','bd','03','01','13','8a','6b'],
['3a','91','11','41','4f','67','dc','ea','97','f2','cf','ce','f0','b4','e6','73'],
['96','ac','74','22','e7','ad','35','85','e2','f9','37','e8','1c','75','df','6e'],
['47','f1','1a','71','1d','29','c5','89','6f','b7','62','0e','aa','18','be','1b'],
['fc','56','3e','4b','c6','d2','79','20','9a','db','c0','fe','78','cd','5a','f4'],
['1f','dd','a8','33','88','07','c7','31','b1','12','10','59','27','80','ec','5f'],
['60','51','7f','a9','19','b5','4a','0d','2d','e5','7a','9f','93','c9','9c','ef'],
['a0','e0','3b','4d','ae','2a','f5','b0','c8','eb','bb','3c','83','53','99','61'],
['17','2b','04','7e','ba','77','d6','26','e1','69','14','63','55','21','0c','7d']]
Rcon = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000,
0x20000000, 0x40000000, 0x80000000, 0x1b000000, 0x36000000]
line = [[0x02, 0x03, 0x01, 0x01],
[0x01, 0x02, 0x03, 0x01],
[0x01, 0x01, 0x02, 0x03],
[0x03, 0x01, 0x01, 0x02]]
Invline = [[0x0e, 0x0b, 0x0d, 0x09],
[0x09, 0x0e, 0x0b, 0x0d],
[0x0d, 0x09, 0x0e, 0x0b],
[0x0b, 0x0d, 0x09, 0x0e]]
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
def trans(c):
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
def transback(num):
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
    a[1] = transback(num % 16)
    a[0] = transback(num//16)
    c = a[0] + a[1]
    return c
def change(c):
    sum = 0
    gamble = 1
    num = []
    for i in range(len(c)):
        num.append(trans(c[i]))
    for i in range(len(c)-1,-1,-1):
        sum = sum + gamble*num[i]
        gamble *=16
    return sum
def changeback(num):
    a = [0,0,0,0,0,0,0,0]
    for i in range(8):
        a[7-i] = transback(num%16)
        num = num//16
    c = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7]
    return c
def changebacktext(num):
    c = ''
    a = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(32):
        a[31 - i] = transback(num % 16)
        num = num // 16
    for i in range(32):
        c = c + a[i]
    return c
def T(c,time):
    #字循环
    res = [c[0]+c[1],c[2]+c[3],c[4]+c[5],c[6]+c[7]]
    temp = res[0]
    res[0] = res[1]
    res[1] = res[2]
    res[2] = res[3]
    res[3] = temp
    #字代换
    result = ''
    for i in range(4):
        m = trans(res[i][0])
        n = trans(res[i][1])
        result = result + S[m][n]
    #相异或
    number = change(result)
    ans = number ^ Rcon[time]
    return ans
def miniT(c):
    res = [c[0] + c[1], c[2] + c[3], c[4] + c[5], c[6] + c[7]]
    result = ''
    for i in range(4):
        m = trans(res[i][0])
        n = trans(res[i][1])
        result = result + S[m][n]
    return result
def generate(key):
    w = []
    for i in range(4):
        c = ''
        for j in range(8):
            c = c + key[i*8+j]
        w.append(c)

    for i in range(4,44):
        if i%4 == 0:
            temp = T(w[i-1],int(i/4)-1)
            ans = change(w[i-4]) ^ temp
        else:
            m = change(w[i-4])
            n = change(w[i-1])
            ans = m^n
        w.append(changeback(ans))
    result = []
    for i in range(11):
        result.append([])
        for j in range(4):
            result[i].append([])
            result[i][j].append(w[4*i][2*j]+w[4*i][2*j+1])
            result[i][j].append(w[4*i+1][2*j]+w[4*i+1][2*j+1])
            result[i][j].append(w[4*i+2][2*j]+w[4*i+2][2*j+1])
            result[i][j].append(w[4*i+3][2*j]+w[4*i+3][2*j+1])
    return result
def generate192(key):
    w = []
    for i in range(6):
        c = ''
        for j in range(8):
            c = c + key[i*8+j]
        w.append(c)

    for i in range(6,52):
        if i%6== 0:
            temp = T(w[i-1],int(i/6)-1)
            ans = change(w[i-6]) ^ temp
        else:
            m = change(w[i-6])
            n = change(w[i-1])
            ans = m^n
        w.append(changeback(ans))
    result = []
    for i in range(13):
        result.append([])
        for j in range(4):
            result[i].append([])
            result[i][j].append(w[4*i][2*j]+w[4*i][2*j+1])
            result[i][j].append(w[4*i+1][2*j]+w[4*i+1][2*j+1])
            result[i][j].append(w[4*i+2][2*j]+w[4*i+2][2*j+1])
            result[i][j].append(w[4*i+3][2*j]+w[4*i+3][2*j+1])
    return result
def generate256(key):
    w = []
    for i in range(8):
        c = ''
        for j in range(8):
            c = c + key[i * 8 + j]
        w.append(c)

    for i in range(8, 60):
        if i % 8 == 0:
            temp = T(w[i - 1], int(i / 8) - 1)
            ans = change(w[i - 8]) ^ temp
        elif i % 8 == 4:
            m = change(miniT(w[i-1]))
            n = change(w[i-8])
            ans = m^n
        else:
            m = change(w[i - 8])
            n = change(w[i - 1])
            ans = m ^ n
        w.append(changeback(ans))
    result = []
    for i in range(15):
        result.append([])
        for j in range(4):
            result[i].append([])
            result[i][j].append(w[4 * i][2 * j] + w[4 * i][2 * j + 1])
            result[i][j].append(w[4 * i + 1][2 * j] + w[4 * i + 1][2 * j + 1])
            result[i][j].append(w[4 * i + 2][2 * j] + w[4 * i + 2][2 * j + 1])
            result[i][j].append(w[4 * i + 3][2 * j] + w[4 * i + 3][2 * j + 1])
    return result
def addKey(text,roundKey):
    result = []
    for i in range(4):
        result.append([])
        for j in range(4):
            a = change(text[i][j])
            b = change(roundKey[i][j])
            ans = a^b
            result[i].append(change_2bits(ans))
    return result
def byteSub(text):
    result = []
    for i in range(4):
        result.append([])
        for j in range(4):
            row = trans(text[i][j][0])
            column = trans(text[i][j][1])
            result[i].append(S[row][column])
    return result
def invByteSub(text):
    result = []
    for i in range(4):
        result.append([])
        for j in range(4):
            row = trans(text[i][j][0])
            column = trans(text[i][j][1])
            result[i].append(InvS[row][column])
    return result
def shiftRow(text):
    for i in range(4):
        for j in range(i):
            text[i].insert(len(text[i]),text[i][0])
            text[i].remove(text[i][0])
    return text
def invShiftRow(text):
    con = [0,3,2,1]
    for i in range(4):
        for j in range(con[i]):
            text[i].insert(len(text[i]),text[i][0])
            text[i].remove(text[i][0])
    return text
def mixColumn(text):
    result = []
    for i in range(4):
        result.append([])
    for i in range(4):
        for j in range(4):
            sum = 0
            for k in range(4):
                sum  = add(sum,mult(line[i][k],change(text[k][j])))
            result[i].append(change_2bits(sum))
    return result
def invMixColumn(text):
    result = []
    for i in range(4):
        result.append([])
    for i in range(4):
        for j in range(4):
            sum = 0
            for k in range(4):
                sum = add(sum, mult(Invline[i][k], change(text[k][j])))
            result[i].append(change_2bits(sum))
    return result
def encrypt(std,time,plaintext,roundKey):
    ciphertext = plaintext
    for i in range(time):
        state = addKey(ciphertext,roundKey[0])
        for j in range(1,std-1):
            afterByteSub = byteSub(state)
            afterShiftRow = shiftRow(afterByteSub)
            afterMixColumn = mixColumn(afterShiftRow)
            state = addKey(afterMixColumn,roundKey[j])
        afterByteSub = byteSub(state)
        afterShiftRow = shiftRow(afterByteSub)
        ciphertext = addKey(afterShiftRow,roundKey[std-1])
    return ciphertext
def decrypt(std,time,ciphertext,roundKey):
    plaintext = ciphertext
    for i in range(time):
        state = addKey(plaintext,roundKey[std-1])
        for j in range(std-2,0,-1):
            afterShiftRow = invShiftRow(state)
            afterByteSub = invByteSub(afterShiftRow)
            state = addKey(afterByteSub,roundKey[j])
            afterMixColumn = invMixColumn(state)
            state = afterMixColumn
        afterShiftRow = invShiftRow(state)
        afterByteSub = invByteSub(afterShiftRow)
        plaintext = addKey(afterByteSub,roundKey[0])
    return plaintext
def AES(std,t,s,k,op):
    if op == 1:
        ans = encrypt(std,t,s,k)
    else:
        ans = decrypt(std,t,s,k)
    print('0x',end = '')
    for i in range(len(ans)):
        print(ans[0][i]+ans[1][i]+ans[2][i]+ans[3][i],end = '')

if __name__ == '__main__':

    length = int(input())
    t = int(input())
    s = input()
    s = s.replace('\n', '')
    s = s.replace('\r', '')
    s = list(s)
    s.pop(0)
    s.pop(0)
    s = [[s[0]+s[1],s[8]+s[9],s[16]+s[17],s[24]+s[25]],[s[2]+s[3],s[10]+s[11],s[18]+s[19],s[26]+s[27]],[s[4]+s[5],s[12]+s[13],s[20]+s[21],s[28]+s[29]],[s[6]+s[7],s[14]+s[15],s[22]+s[23],s[30]+s[31]]]
    k = input()
    k = k.replace('\n', '')
    k = k.replace('\r', '')
    k = list(k)
    k.pop(0)
    k.pop(0)
    op = int(input())
    if length == 192:
        std = 13
        keylist = generate192(k)
    else:
        std = 15
        keylist = generate256(k)
    AES(std,t,s,keylist,op)