def decode(s):
    max = 0
    letter = 0
    for i in range(0,25):
        appear  = s.count(chr(i+97))
        if appear > max :
            max = appear
            letter = i
    k = (26+letter-4)%26
    print(k)


if __name__ == '__main__':
    s = input()
    decode(s)