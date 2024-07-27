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
def fast_mode(M,e,N):
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
    print(powers[len(D)-1])
if __name__ == '__main__':
    M,e,N = map(int,input().split())
    fast_mode(M,e,N)
