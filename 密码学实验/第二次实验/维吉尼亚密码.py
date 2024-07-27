def encrypt(plaintext, key):
    s1 = list(plaintext)
    for i in range(len(plaintext)):
        j = i % len(key)
        s1[i] = chr((ord(s1[i]) + ord(key[j]) - 194) % 26 + 97)
    s = ''.join(s1)
    print(s)


def decrypt(ciphertext, key):
    s1 = list(ciphertext)
    for i in range(len(ciphertext)):
        j = i % len(key)
        s1[i] = chr((ord(s1[i]) - ord(key[j])) % 26 + 97)
    s = ''.join(s1)
    print(s)

def Vigenere(s,key,mod):
    if mod == 1:
        encrypt(s, key)
    else:
        decrypt(s, key)


if __name__ == '__main__':
    key = input()
    s = input()
    key = key.replace('\n','')
    key = key.replace('\r','')
    s = s.replace('\n','')
    s = s.replace('\r','')
    mod = int(input())
    Vigenere(s, key, mod)
