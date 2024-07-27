f = 1812433253
n = 624
r = 31
m = 397
lower_mask = (1 << r)-1
upper_mask = ~lower_mask
a = 0x9908B0DF
d = 0xFFFFFFFF
u = 11
s = 7
b = 0x9D2C5680
c = 0xEFC60000
t = 15
l = 18
MT = []
def seedInit(seed):
    MT.append(seed)
    for i in range(1,n):
        MT.append(0xFFFFFFFF & (f * (MT[i-1] ^ (MT[i-1] >> (32-2)))+i))
def twist():
    for i in range(n):
        x = (MT[i]&upper_mask) + (MT[(i+1)%n]&lower_mask)
        xA = x >> 1
        if x % 2 !=0 :
            xA = xA ^ a
        MT[i] = MT[(i+m) % n] ^ xA
def extract(index):
    if index >= n:
        twist()
    x = MT[index]
    y = x ^((x>>u)&d)
    y = y^((y<<s)&b)
    y = y ^ ((y << t) & c)
    z = y ^ (y>>l)
    return z&d
def Mersenne(seed):
    seedInit(seed)
    twist()
    for i in range(20):
        print(extract(i))
if __name__ == '__main__':
    seed = int(input())
    Mersenne(seed)