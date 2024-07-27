def add(a,b):
    return  a^b
def mult(a,b):
    result = 0
    while b>0:
        if b%2 == 1:
            result ^= a
        a = gmul(a,0x11b)
        b >>= 1
    return result
def gmul(a,poly):
    a <<= 1
    if a&0x100 == 0x100:
        a ^= poly
    return a & 0xff
def div(a,b):
    q = 0
    while a.bit_length() >= b.bit_length():
        rec = a.bit_length()- b.bit_length()
        a ^= (b << rec)
        q ^= (1 << rec)
    return q,a
def exEuclid(a,b):
    if b == 0:
        return a, 1, 0
    else:
        q,r = div(a,b)
        GCD,xtmp,ytmp = exEuclid(b,r)
        x = ytmp
        y = xtmp ^ mult(ytmp,q)
        return GCD,x,y
a = int(input(),16)
b = 0x11b
GCD,x,y = exEuclid(a,b)
print('%02x' %x)