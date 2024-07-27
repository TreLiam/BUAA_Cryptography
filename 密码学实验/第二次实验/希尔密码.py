def exEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        q = a // b
        r = a % b
        GCD, xtmp, ytmp = exEuclid(b, r)
        x = ytmp
        y = xtmp - (q) * ytmp
        if GCD < 0:
            x = -x
            y = -y
            GCD = -GCD
        while x <= 0:
            x += abs(b) // GCD
            y = (GCD - a * x) // b
        return GCD, x, y
def getInversion(numlist):
    count = 0
    for i in range(1, len(numlist)):
        subscript = numlist[i]
        for j in range(i):
            if subscript < numlist[j]:
                count += 1
    return count


D = 0


# 全排列，求每项的积
def permutation(dd, ilist, jlist, index):
    global D
    for i in range(index, len(jlist)):
        if index == len(jlist) - 1:
            term = 1
            for ii in range(len(ilist)):
                i = ilist[ii]
                j = jlist[ii]
                term *= dd[i][j]
            if getInversion(jlist) % 2 == 0:
                D += term
            else:
                D -= term
            return
        tmp = jlist[index]
        jlist[index] = jlist[i]
        jlist[i] = tmp
        permutation(dd, ilist, jlist, index + 1)
        tmp = jlist[index]
        jlist[index] = jlist[i]
        jlist[i] = tmp


def det(dd):
    jlist = []
    ilist = []
    for ii in range(len(dd)):
        ilist.append(ii)
        jlist.append(ii)
    permutation(dd, ilist, jlist, 0)

def getInv(key,n):
    global D
    keylist = []
    det(key)
    GCD, x, y = exEuclid(D, 26)
    for i in range(n):
        keylist.append([])
        for k in range(n):
            list = []
            line = 0
            for j in range(n):
                if j == i :
                    continue
                else:
                    list.append([])
                    for l in range(n):
                        if l == k:
                            continue
                        else:
                            list[line].append(key[j][l])
                    line += 1
            D = 0
            det(list)
            keylist[i].append(((D%26) * x)% 26)
    for i in range(n):
        for j in range(i,n):
            t = keylist[i][j]
            keylist[i][j] = keylist[j][i]
            keylist[j][i] = t
    for i in range(n):
        for j in range(n):
            keylist[i][j] = (pow(-1,i+j)*keylist[i][j])%26
    return keylist

def encrypt(plaintext, key, n):
    message = []
    for i in range(len(plaintext) // n):
        message.append([])
        for k in range(n):
            message[i].append(ord(plaintext[k + i * n]) - 97)
    code = []
    for i in range(len(message)):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += key[k][j] * message[i][k]
            sum %= 26
            code.append(chr(sum + 97))
    ciphertext = ''.join(code)
    print(ciphertext)


def decrypt(ciphertext, key, n):
    keylist = (getInv(key,n))
    message = []
    for i in range(len(ciphertext) // n):
        message.append([])
        for k in range(n):
            message[i].append(ord(ciphertext[k + i * n]) - 97)
    code = []
    for i in range(len(message)):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += keylist[k][j] * message[i][k]
            sum %= 26
            code.append(chr(sum + 97))
    plaintext = ''.join(code)
    print(plaintext)


def Hill(message, key, mod, n):
    if mod == 1:
        encrypt(message, key, n)
    else:
        decrypt(message, key, n)


if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([])
        key = input()
        keylist = key.split(' ')
        for k in range(n):
            matrix[i].append(int(keylist[k]))
    s = input()
    mod = int(input())
    Hill(s, matrix, mod, n)
