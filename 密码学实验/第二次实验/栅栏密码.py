def encrypt(row,plaintext):
    a = []
    for i in range(row):
        a.append([])
    for i in range(len(plaintext)):
        j = i % row
        a[j].append(plaintext[i])
    ciphertext = ''
    for i in range(row):
        text =''.join(a[i])
        ciphertext = ciphertext + text
    print(ciphertext)

def decrypt(row,ciphertext):
    a = []
    for i in range(row):
        a.append([])
    m = len(ciphertext) // row
    n = len(ciphertext) % row
    j = 0
    for i in range(row):
        if i < n:
            for k in range(m+1):
                a[i].append(ciphertext[j])
                j += 1
        else:
            for k in range(m):
                a[i].append(ciphertext[j])
                j += 1
            a[i].append('*')
    plaintext = ''
    for i in range(m+1):
        for k in range(row):
            plaintext = plaintext + a[k][i]
    plaintext = plaintext.replace('*','')
    print(plaintext)

def RailfenceCipher(k,s,mod):
    if mod == 1:
        encrypt(k, s)
    else:
        decrypt(k, s)


if __name__ == '__main__':
    k = int(input())
    s = input()
    s = s.replace('\n','')
    s = s.replace('\r','')
    mod = int(input())
    RailfenceCipher(k, s, mod)