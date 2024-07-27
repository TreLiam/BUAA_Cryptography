import gmpy2
def Exgcd(a,b):
    if b==0:
        return 1,0,a
    else:
        x,y,q = Exgcd(b,a%b)
        x,y = y,(x - (a//b)*y)
        return x,y,q
def sun(a,m):
    e = []
    result = 0
    M = 1
    for i in range(len(m)):
        e.append(0)
        M = M * m[i]   #累乘
    for i in range(len(m)):
        j=Exgcd(M//m[i],m[i])  #求逆元
        e[i] = j[0]
        result = result + (M//m[i]) * e[i] * a[i]
    ans = int(result)
    if ans == 0:
        ans = abs(m[0] * m[1] * m[2])
    else:
        ans = ans % abs(m[0] * m[1] * m[2])
    return ans
def attack(C,N,e):
    ans = sun(C,N)
    M = gmpy2.iroot(ans,e)
    return M[0]
if __name__ == '__main__':
    n = int(input())
    e = int(input())
    C = []
    N = []
    for i in range(n):
        c = int(input())
        C.append(c)
        mod = int(input())
        N.append(mod)
    print(attack(C,N,e))