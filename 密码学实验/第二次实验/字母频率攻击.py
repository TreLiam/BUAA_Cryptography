def ReadFile():
    with open("ciphertext.txt",'r') as f:
        data = f.read()
        return data

def Count(data):
    keylist = []
    for i in range(26):
        keylist.append(0)
    for i in range(len(data)):
        keylist[ord(data[i]) - 97] += 1
    return keylist

def decode(data,alpha):

    s = list(data)
    for i in range(len(s)):
        s[i] = chr(alpha.index(ord(s[i]) - 97) + 97)
    plaintext = ''.join(s)
    with open("plaintext.txt","w") as file:
        file.write(plaintext)
def swap(a,b):
    t = a
    a = b
    b = t
    return a,b


if __name__ == '__main__':
    begin = 'etaoinshrdlcumwfgypbvkjxqz'
    keylist = []
    data  = ReadFile()
    keylist = Count(data)
    print(keylist)
    a = list(begin)
    key = []
    for i in range(26):
        key.append(0)
    for i in range(26):
        place = keylist.index(max(keylist))
        keylist[place] = -1
        key[ord(a[i]) - 97] = place
    print(key)
    key[ord('s') - 97], key[ord('h') - 97]  = swap(key[ord('s')-97],key[ord('h')-97])
    key[ord('i') - 97], key[ord('n') - 97] = swap(key[ord('i') - 97], key[ord('n') - 97])
    key[ord('m') - 97], key[ord('u') - 97] = swap(key[ord('m') - 97], key[ord('u') - 97])
    key[ord('c') - 97], key[ord('u') - 97] = swap(key[ord('c') - 97], key[ord('u') - 97])
    key[ord('j') - 97], key[ord('x') - 97] = swap(key[ord('j') - 97], key[ord('x') - 97])
    print(key)
    decode(data,key)