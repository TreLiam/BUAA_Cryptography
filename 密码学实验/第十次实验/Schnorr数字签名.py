from hashlib import sha1
def fastMode(base,expo,p):
    ans = 1
    while expo > 0:
        a = expo % 2
        expo = expo >> 1
        if a == 1:
            ans = (ans * base) % p
        base = (base * base) % p
    return ans
def Sign_Schnorr(p,q,a,M,Mode):
    if Mode == 'Sign':
        s = int(input())
        r = int(input())
        x = str(fastMode(a,r,p))
        message = M + x
        e = eval('0x' + sha1(message.encode('utf-8')).hexdigest())
        y = (r + s*e) % q
        print(e,y)
    else:
        v = int(input())
        e,y = map(int, input().split())
        _x = str((fastMode(a,y,p) * fastMode(v,e,p)) % p)
        message = M + _x
        _e = eval('0x' + sha1(message.encode('utf-8')).hexdigest())
        if e == _e:
            print('True')
        else:
            print('False')
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    a = int(input())
    M = input()
    Mode = input()
    Sign_Schnorr(p,q,a,M,Mode)