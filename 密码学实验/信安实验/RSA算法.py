import random

from functools import reduce
import operator
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
def fastMode(M,e,N):
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
#求最大公因数
def gcd(a, b):
    if a < b:
        t = a
        a = b
        b = t
    while True:
        temp = a % b
        if temp:
            a = b
            b = temp
        else:
            break
    return b
#Millar-Rabin 素性检测法
def Miller_Rabin(n):
    if n % 2 == 0:
        return 0
    temp = n - 1
    k = 0
    flag = 0
    while temp % 2 == 0:
        temp = temp // 2
        k = k + 1
    q = temp  # n-1=2^k*q
    for i in range(80):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1:
            return 0
        if pow(a, q, n) != 1:
            flag = flag + 1
        for j in range(k):
            if pow(a, (2 ** j) * q, n) != n - 1:
                flag = flag + 1

        if flag == k + 1:
            return 0
        flag = 0
    return 1
#欧几里得算法
def exEuclid(a,b,m):
    if b == 0:
        m[0] = a
        m[1] = 1
        m[2] = 0
        return m
    else:
        exEuclid(b,a%b,m)
        GCD = m[0]
        xtmp = m[1]
        ytmp = m[2]
        x = ytmp
        y = xtmp - (a//b) * ytmp
        if GCD < 0:
            x = -x
            y = -y
            GCD = -GCD
        while x <= 0:
            x += abs(b) // GCD
            y = (GCD - a*x) // b
        m[0] = GCD
        m[1] = x
        m[2] = y
        return m
def encrypt(M,e,n):
    ciphertext = mont(M,e,n)
    return ciphertext
def decrypt(c,d,n,p,q,m):
    a = d % (p-1)
    b = d % (q-1)
    Vp = mont(c,a,p)
    Vq = mont(c,b,q)

    m = [0,0,0]
    m = exEuclid(q,p,m)
    inv_q = m[1]
    Xp = q * inv_q

    m = [0,0,0]
    m = exEuclid(p, q, m)
    inv_p = m[1]
    Xq = p * inv_p

    plaintext = (Vp * Xp + Vq * Xq) % n
    return plaintext
def RSA(p,q,e,M,op):
    n = p * q
    if op == 1:
        ciphertext = encrypt(M,e,n)
        print(ciphertext)
    else :
        m = [0,0,0]
        Euler_n = (p-1)*(q-1)
        m = exEuclid(e,Euler_n,m)
        d = m[1]
        plaintext = decrypt(M,d,n,p,q,m)
        print(plaintext)
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    e = int(input())
    m = int(input())
    op = int(input())
    if Miller_Rabin(p) == 0:
        print("Mole ! Terminate !")
    elif Miller_Rabin(q) == 0:
        print("Mole ! Terminate !")
    else:
        RSA(p,q,e,m,op)
