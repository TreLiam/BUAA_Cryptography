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
def invert(a,b):
    m = [0,0,0]
    result = exEuclid(a,b,m)
    return result[1]
def add(Ax,Ay,Bx,By,p,a):
    if (Ax == Bx)&(Ay == By):
        m = ((3 * Ax * Ax + a)*invert(2*Ay,p)) % p
    else:
        m = ((By - Ay) * invert(Bx - Ax, p)) % p
    Rx = (m * m - Ax - Bx) % p
    Ry = (m*(Ax - Rx) - Ay) % p
    return Rx,Ry
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
def fast_mult(p,a,b,Ax,Ay,k):
    D = creat_Link(k)
    multers = [(Ax,Ay)]
    for k in range(1,len(D)):
        if D[k] % 2 == 0:
            sp = D.index(D[k] // 2)
            multers.append(add(multers[sp][0],multers[sp][1],multers[sp][0],multers[sp][1],p,a))
        else:
            i = k - 1
            j = D.index(D[k] - D[i])
            multers.append(add(multers[i][0],multers[i][1],multers[j][0],multers[j][1],p,a))
    print(multers[len(D)-1])
if __name__ == '__main__':
    p = int(input())
    a = int(input())
    b = int(input())
    Ax,Ay = map(int,input().split())
    k = int(input())
    fast_mult(p,a,b,Ax,Ay,k)
