def encrypt(plaintext,key):
    s1 = list(plaintext)
    for i in range(len(s1)):
        j = i % len(key)
        s1[i] = chr(ord(s1[i]) ^ ord(key[j]))
    ciphertext = ''.join(s1)
    print(ciphertext)

def decrypt(ciphertext,key):
    s1 = list(ciphertext)
    for i in range(len(s1)):
        j = i % len(key)
        s1[i] = chr(ord(s1[i]) ^ ord(key[j]))
    plaintext = ''.join(s1)
    print(plaintext)


def Vernam(key,s,mod):
    if mod == 1:
        encrypt(s, key)
    else:
        decrypt(s, key)


if __name__ == '__main__':
    key = input()
    key = key.replace('\n','')
    key = key.replace('\r','')
    s = input()
    s = s.replace('\n','')
    s = s.replace('\r','')
    mod = int(input())
    Vernam(key, s, mod)