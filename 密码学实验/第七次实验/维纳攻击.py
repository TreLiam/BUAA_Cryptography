import gmpy2
#转为连分数
def transform(x,y):
    res = []
    while y:
        res.append(x // y)
        x, y = y, x % y
    return res
#算出渐进分数
def getlist(res):
    ans = [[res[0],1]]
    for i in range(1,len(res)):
        div = [1,res[i]]
        for j in range(i-1,-1,-1):
            mid = div[1] * res[j] + div[0]
            div[0] = div[1]
            div[1] = mid
        mid = div[0]
        div[0] = div[1]
        div[1] = mid
        ans.append(div)
    return ans
def solve_function(N,Euler_N):
    b = N-Euler_N+1
    mid = (pow(b,2) - 4 * N)
    p = (-1 * b - gmpy2.isqrt(mid))// 2
    q = (-1 * b + gmpy2.isqrt(mid)) // 2
    return p,q
def Winere_Attack(e,N):
    res = transform(e,N)
    ans = getlist(res)
    for i in range(len(ans)):
        k = ans[i][0]
        d = ans[i][1]
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        Euler_N = (e * d - 1) // k
        p,q = solve_function(N,Euler_N)
        if p * q == N:
            p = abs(p)
            q = abs(q)
            if p > q:
                mid = p
                p = q
                q = mid
            return p,q,d
if __name__ == '__main__':
    e = int(input())
    N = int(input())
    p,q,d = Winere_Attack(e,N)
    print(p)
    print(q)
    print(d)