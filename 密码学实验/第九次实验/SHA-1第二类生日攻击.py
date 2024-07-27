from hashlib import sha1
def attack2(string1,string2,string3):
    h1 = sha1(string1.encode('utf-8')).hexdigest()
    h2 = sha1(string2.encode('utf-8')).hexdigest()
    h3 = sha1(string3.encode('utf-8')).hexdigest()
    for i in range(100000000):
        string = "I have {} rmb.".format(i)
        h = sha1(string.encode('utf-8')).hexdigest()
        if h1[:6] == h[:6]:
            print(string1)
            print(string)
        if h2[:6] == h[:6]:
            print(string2)
            print(string)
        if h3[:6] == h[:6]:
            print(string3)
            print(string)
if __name__ == '__main__':
    string1 = "I have 1.00 rmb."
    string2 = "I have 0.00 rmb."
    string3 = "I have 1.01 rmb."
    attack2(string1,string2,string3)