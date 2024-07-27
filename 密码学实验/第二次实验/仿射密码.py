def exEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        q = a // b
        r = a % b
        GCD, xtmp, ytmp = exEuclid(b, r)
        x = ytmp
        y = xtmp - (q) * ytmp
        return GCD, x, y


def encrypt(k, b, s1):
    lenth = len(s1)
    for i in range(lenth):
        s1[i] = chr((k * (ord(s1[i]) - 97) + b) % 26 + 97)
    s = ''.join(s1)
    s.strip()
    print(s)


def decrypt(k, b, s1):
    GCD, x, y = exEuclid(k, 26)
    lenth = len(s1)
    for i in range(lenth):
        s1[i] = chr((x * ((ord(s1[i]) - 97) - b)) % 26 + 97)
    s = ''.join(s1)
    s.strip()
    print(s)


def Affine(k, b, s, mod):
    if (len(s) <= 400) & (k <= 25) & (k >= 1) & (b <= 25) & (b >= 1) & (k % 2 != 0) & (k != 13):
        if mod == 1:
            encrypt(k, b, s1)
        else:
            decrypt(k, b, s1)
    else:
        print('invalid key')


if __name__ == '__main__':
    k, b = map(int, input().split())
    s = input()
    s = s.replace('\n', '')
    s = s.replace('\r', '')
    s1 = list(s)
    mod = int(input())
    Affine(k, b, s, mod)
