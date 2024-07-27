def encrypt(plaintext, keyBox, invKeyBox):
    s1 = list(plaintext)
    for i in range(len(s1)):
        place = keyBox.find(s1[i])
        s1[i] = invKeyBox[place]
    s = ''.join(s1)
    print(s)

def decrypt(ciphertext, keyBox, invKeyBox):
    s1 = list(ciphertext)
    for i in range(len(s1)):
        place = invKeyBox.find(s1[i])
        s1[i] = keyBox[place]
    s = ''.join(s1)
    print(s)


def MonoSubCipher(s,keyBox,invKeyBox,mod):
    if mod == 1:
        encrypt(s,keyBox,invKeyBox)
    else:
        decrypt(s,keyBox,invKeyBox)


if __name__ == '__main__':
    keyBox = input()
    invKeyBox = input()
    s = input()
    mod = int(input())
    MonoSubCipher(s, keyBox, invKeyBox, mod)