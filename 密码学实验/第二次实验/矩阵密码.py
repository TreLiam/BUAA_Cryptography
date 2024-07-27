def encrypt(row,key,plaintext):
    a = []
    for i in range(row):
        a.append([])
    for i in range(len(plaintext)):
        j = ord(key[i%row]) - 49
        a[j].append(plaintext[i])
    ciphertext = ''
    for i in range(row):
        text =''.join(a[i])
        ciphertext = ciphertext + text
    print(ciphertext)

def decrypt(row,key,ciphertext):
    a = []
    for i in range(row):
        a.append([])
    m = len(ciphertext) // row
    n = len(ciphertext) % row
    if n !=0:
        m += 1
        for i in range(row - n):
            ciphertext += '*'
    j = 0
    for i in range(row):
        for k in range(m):
            a[key.find(str(i+1))].append(ciphertext[j])
            j += 1
    plaintext = ''
    for i in range(m):
        for k in range(row):
            plaintext = plaintext + a[k][i]
    plaintext = plaintext.replace('*','')
    print(plaintext)

def RailfenceCipher(n,k,s,mod):
    if mod == 1:
        encrypt(n,k, s)
    else:
        decrypt(n,k, s)


if __name__ == '__main__':
    n = int(input())
    k = input()
    s = input()
    s = s.replace('\n','')
    s = s.replace('\r','')
    mod = int(input())
    RailfenceCipher(n,k, s, mod)