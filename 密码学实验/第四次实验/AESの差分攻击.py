def regulation(s):
    s = s.replace('\n', '')
    s = s.replace('\r', '')
    s = list(s)
    s.pop(0)
    s.pop(0)
    s = [[s[0]+s[1],s[8]+s[9],s[16]+s[17],s[24]+s[25]],[s[2]+s[3],s[10]+s[11],s[18]+s[19],s[26]+s[27]],[s[4]+s[5],s[12]+s[13],s[20]+s[21],s[28]+s[29]],[s[6]+s[7],s[14]+s[15],s[22]+s[23],s[30]+s[31]]]
    return s
b0 = [0,7,10,13]
b1 = [1,4,11,14]
b2 = [2,5,8,15]
b3 = [3,6,9,12]
b4 = [3,6,9,12]
b5 = [0,7,10,13]
b6 = [1,4,11,14]
b7 = [2,5,8,15]
b8 = [2,5,8,15]
b9 = [3,6,9,12]
b10 = [0,7,10,13]
b11 = [1,4,11,14]
b12 = [1,4,11,14]
b13 = [2,5,8,15]
b14 = [3,6,9,12]
b15 = [0,7,10,13]

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
def xor(a,b):
    n = change(a)
    m = change(b)
    ans = change_2bits(m^n)
    return ans
if __name__ == '__main__':
    plaintext = input()
    ciphertext = input()
    plaintext = regulation(plaintext)
    ciphertext = regulation(ciphertext)
    attack = []
    for i in range(16):
        attack.append([])
        for j in range(10):
            result = []
            text = input()
            text = regulation(text)
            for k in range(4):
                for m in range(4):
                    if xor(ciphertext[k][m],text[k][m])!='00':
                        result.append(xor(ciphertext[k][m],text[k][m]))
            attack[i].append(result)
    for i in range(10):
        print(attack[0][i])


