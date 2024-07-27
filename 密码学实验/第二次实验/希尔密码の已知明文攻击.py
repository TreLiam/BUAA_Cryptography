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

def getInv(key,n): #求逆矩阵
    global D
    keylist = []
    D = 0
    det(key)
    GCD, x, y = exEuclid(D%26, 26)
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
            keylist[i].append(D*pow(-1,i+k))
    for i in range(n):
        for j in range(i,n):
            t = keylist[i][j]
            keylist[i][j] = keylist[j][i]
            keylist[j][i] = t
    for i in range(n):
        for j in range(n):
            keylist[i][j] = (keylist[i][j] * x) % 26
    return keylist

def decode(n,m,c):
    for j in range(0,len(m),n*n):
        plaintext = []
        ciphertext = []
        for i in range(n):
            plaintext.append([])
            ciphertext.append([])
            for k in range(n):
                plaintext[i].append(ord(m[i*n+k+j])-97)
                ciphertext[i].append(ord(c[i*n+k+j])-97)
        global D
        D = 0
        det(plaintext)
        GCD,x,y = exEuclid(D,26)
        if GCD == 1:
            break
    keylist = getInv(plaintext,n)

    for i in range(n):
        for k in range(n):
            sum = 0
            for j in range(n):
                sum = sum + keylist[i][j] * ciphertext[j][k]
            print(sum%26,end = ' ')
        print()


if __name__ == '__main__':
    n = int(input())
    m = input()
    c = input()
    decode(n,m,c)
