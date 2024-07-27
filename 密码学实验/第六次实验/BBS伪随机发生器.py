def BitToInt(bitcoin):
    sum = 0
    bet = 1
    for i in range(len(bitcoin)):
        sum = sum + bitcoin[i]*bet
        bet = bet*2
    return sum
def getBBS(lenth,p,q,s):
    x = []
    b = []
    n = p*q
    x.append((s*s)%n)
    for i in range(1,lenth+1):
        x.append((x[i-1]*x[i-1])%n)
        b.append(x[i]%2)
    print(BitToInt(b))
if __name__ == '__main__':
    lenth = int(input())
    p = int(input())
    q = int(input())
    s = int(input())
    getBBS(lenth,p,q,s)