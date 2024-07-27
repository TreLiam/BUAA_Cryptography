from hashlib import sha1
def attack1(n,H):
    i = 0
    while True:
        test = str(i)
        h = sha1(test.encode('utf-8')).hexdigest()
        if h[:n // 4] == H[:n // 4]:
            print(test)
            break
        i = i + 1
if __name__ == '__main__':
    n = int(input())
    H = input().strip()
    attack1(n,H)