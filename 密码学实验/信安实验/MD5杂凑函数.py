import time
initialState = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
def rotlFixed(x, n):
    return (x << n) | ((x >> (32 - n)) & 0xffffffff)
def fill(sequence):
    '将字节序列按小端序填充成512位【16整数*4字节】的倍数'
    count=len(sequence)
    multi_16s=((count+8)//64+1)*16              # 共需要整数的个数，每个整数存储4个字节的数据
    sequence+=[0]*(multi_16s*4-count)           # 用 0 填充
    sequence[count] |= 128                      # 用一个 1 补在后面
    multi_4bytes=[]
    for i in range(len(sequence)//4):
        sequence[i*4+3],sequence[i*4+2],sequence[i*4+1],sequence[i*4]=tuple(sequence[i*4:(i+1)*4])              # 大端序存储
        multi_4bytes.append(int("".join(["{:08b}".format(ii) for ii in sequence[i*4:(i+1)*4]]),2))              # 每四个Ascii合并成一个4字节整数
    multi_4bytes[-2],multi_4bytes[-1]=int("{:064b}".format(count*8)[32:],2),int("{:064b}".format(count*8)[:32],2)
    return multi_4bytes
def MD5_F1(x, y, z):
    return x & y | (~x) & z
def MD5_F2(x, y, z):
    return MD5_F1(z, x, y)
def MD5_F3(x, y, z):
    return x ^ y ^ z
def MD5_F4(x, y, z):
    return y ^ (x | (~z))
def MD5_STEP(f, w, x, y, z, data, s):
    return (rotlFixed((w + f(x, y, z) + data) & 0xffffffff, s) + x) & 0xffffffff
def MD5_TRANSFORM(digestlist, inputlist):
    a = digestlist[0]
    b = digestlist[1]
    c = digestlist[2]
    d = digestlist[3]
    a = MD5_STEP(MD5_F1, a, b, c, d, (inputlist[0] + 0xd76aa478) & 0xffffffff, 7)
    d = MD5_STEP(MD5_F1, d, a, b, c, (inputlist[1] + 0xe8c7b756) & 0xffffffff, 12)
    c = MD5_STEP(MD5_F1, c, d, a, b, (inputlist[2] + 0x242070db) & 0xffffffff, 17)
    b = MD5_STEP(MD5_F1, b, c, d, a, (inputlist[3] + 0xc1bdceee) & 0xffffffff, 22)
    a = MD5_STEP(MD5_F1, a, b, c, d, (inputlist[4] + 0xf57c0faf) & 0xffffffff, 7)
    d = MD5_STEP(MD5_F1, d, a, b, c, (inputlist[5] + 0x4787c62a) & 0xffffffff, 12)
    c = MD5_STEP(MD5_F1, c, d, a, b, (inputlist[6] + 0xa8304613) & 0xffffffff, 17)
    b = MD5_STEP(MD5_F1, b, c, d, a, (inputlist[7] + 0xfd469501) & 0xffffffff, 22)
    a = MD5_STEP(MD5_F1, a, b, c, d, (inputlist[8] + 0x698098d8) & 0xffffffff, 7)
    d = MD5_STEP(MD5_F1, d, a, b, c, (inputlist[9] + 0x8b44f7af) & 0xffffffff, 12)
    c = MD5_STEP(MD5_F1, c, d, a, b, (inputlist[10] + 0xffff5bb1) & 0xffffffff, 17)
    b = MD5_STEP(MD5_F1, b, c, d, a, (inputlist[11] + 0x895cd7be) & 0xffffffff, 22)
    a = MD5_STEP(MD5_F1, a, b, c, d, (inputlist[12] + 0x6b901122) & 0xffffffff, 7)
    d = MD5_STEP(MD5_F1, d, a, b, c, (inputlist[13] + 0xfd987193) & 0xffffffff, 12)
    c = MD5_STEP(MD5_F1, c, d, a, b, (inputlist[14] + 0xa679438e) & 0xffffffff, 17)
    b = MD5_STEP(MD5_F1, b, c, d, a, (inputlist[15] + 0x49b40821) & 0xffffffff, 22)
    a = MD5_STEP(MD5_F2, a, b, c, d, (inputlist[1] + 0xf61e2562) & 0xffffffff, 5)
    d = MD5_STEP(MD5_F2, d, a, b, c, (inputlist[6] + 0xc040b340) & 0xffffffff, 9)
    c = MD5_STEP(MD5_F2, c, d, a, b, (inputlist[11] + 0x265e5a51) & 0xffffffff, 14)
    b = MD5_STEP(MD5_F2, b, c, d, a, (inputlist[0] + 0xe9b6c7aa) & 0xffffffff, 20)
    a = MD5_STEP(MD5_F2, a, b, c, d, (inputlist[5] + 0xd62f105d) & 0xffffffff, 5)
    d = MD5_STEP(MD5_F2, d, a, b, c, (inputlist[10] + 0x02441453) & 0xffffffff, 9)
    c = MD5_STEP(MD5_F2, c, d, a, b, (inputlist[15] + 0xd8a1e681) & 0xffffffff, 14)
    b = MD5_STEP(MD5_F2, b, c, d, a, (inputlist[4] + 0xe7d3fbc8) & 0xffffffff, 20)
    a = MD5_STEP(MD5_F2, a, b, c, d, (inputlist[9] + 0x21e1cde6) & 0xffffffff, 5)
    d = MD5_STEP(MD5_F2, d, a, b, c, (inputlist[14] + 0xc33707d6) & 0xffffffff, 9)
    c = MD5_STEP(MD5_F2, c, d, a, b, (inputlist[3] + 0xf4d50d87) & 0xffffffff, 14)
    b = MD5_STEP(MD5_F2, b, c, d, a, (inputlist[8] + 0x455a14ed) & 0xffffffff, 20)
    a = MD5_STEP(MD5_F2, a, b, c, d, (inputlist[13] + 0xa9e3e905) & 0xffffffff, 5)
    d = MD5_STEP(MD5_F2, d, a, b, c, (inputlist[2] + 0xfcefa3f8) & 0xffffffff, 9)
    c = MD5_STEP(MD5_F2, c, d, a, b, (inputlist[7] + 0x676f02d9) & 0xffffffff, 14)
    b = MD5_STEP(MD5_F2, b, c, d, a, (inputlist[12] + 0x8d2a4c8a) & 0xffffffff, 20)
    a = MD5_STEP(MD5_F3, a, b, c, d, (inputlist[5] + 0xfffa3942) & 0xffffffff, 4)
    d = MD5_STEP(MD5_F3, d, a, b, c, (inputlist[8] + 0x8771f681) & 0xffffffff, 11)
    c = MD5_STEP(MD5_F3, c, d, a, b, (inputlist[11] + 0x6d9d6122) & 0xffffffff, 16)
    b = MD5_STEP(MD5_F3, b, c, d, a, (inputlist[14] + 0xfde5380c) & 0xffffffff, 23)
    a = MD5_STEP(MD5_F3, a, b, c, d, (inputlist[1] + 0xa4beea44) & 0xffffffff, 4)
    d = MD5_STEP(MD5_F3, d, a, b, c, (inputlist[4] + 0x4bdecfa9) & 0xffffffff, 11)
    c = MD5_STEP(MD5_F3, c, d, a, b, (inputlist[7] + 0xf6bb4b60) & 0xffffffff, 16)
    b = MD5_STEP(MD5_F3, b, c, d, a, (inputlist[10] + 0xbebfbc70) & 0xffffffff, 23)
    a = MD5_STEP(MD5_F3, a, b, c, d, (inputlist[13] + 0x289b7ec6) & 0xffffffff, 4)
    d = MD5_STEP(MD5_F3, d, a, b, c, (inputlist[0] + 0xeaa127fa) & 0xffffffff, 11)
    c = MD5_STEP(MD5_F3, c, d, a, b, (inputlist[3] + 0xd4ef3085) & 0xffffffff, 16)
    b = MD5_STEP(MD5_F3, b, c, d, a, (inputlist[6] + 0x04881d05) & 0xffffffff, 23)
    a = MD5_STEP(MD5_F3, a, b, c, d, (inputlist[9] + 0xd9d4d039) & 0xffffffff, 4)
    d = MD5_STEP(MD5_F3, d, a, b, c, (inputlist[12] + 0xe6db99e5) & 0xffffffff, 11)
    c = MD5_STEP(MD5_F3, c, d, a, b, (inputlist[15] + 0x1fa27cf8) & 0xffffffff, 16)
    b = MD5_STEP(MD5_F3, b, c, d, a, (inputlist[2] + 0xc4ac5665) & 0xffffffff, 23)
    a = MD5_STEP(MD5_F4, a, b, c, d, (inputlist[0] + 0xf4292244) & 0xffffffff, 6)
    d = MD5_STEP(MD5_F4, d, a, b, c, (inputlist[7] + 0x432aff97) & 0xffffffff, 10)
    c = MD5_STEP(MD5_F4, c, d, a, b, (inputlist[14] + 0xab9423a7) & 0xffffffff, 15)
    b = MD5_STEP(MD5_F4, b, c, d, a, (inputlist[5] + 0xfc93a039) & 0xffffffff, 21)
    a = MD5_STEP(MD5_F4, a, b, c, d, (inputlist[12] + 0x655b59c3) & 0xffffffff, 6)
    d = MD5_STEP(MD5_F4, d, a, b, c, (inputlist[3] + 0x8f0ccc92) & 0xffffffff, 10)
    c = MD5_STEP(MD5_F4, c, d, a, b, (inputlist[10] + 0xffeff47d) & 0xffffffff, 15)
    b = MD5_STEP(MD5_F4, b, c, d, a, (inputlist[1] + 0x85845dd1) & 0xffffffff, 21)
    a = MD5_STEP(MD5_F4, a, b, c, d, (inputlist[8] + 0x6fa87e4f) & 0xffffffff, 6)
    d = MD5_STEP(MD5_F4, d, a, b, c, (inputlist[15] + 0xfe2ce6e0) & 0xffffffff, 10)
    c = MD5_STEP(MD5_F4, c, d, a, b, (inputlist[6] + 0xa3014314) & 0xffffffff, 15)
    b = MD5_STEP(MD5_F4, b, c, d, a, (inputlist[13] + 0x4e0811a1) & 0xffffffff, 21)
    a = MD5_STEP(MD5_F4, a, b, c, d, (inputlist[4] + 0xf7537e82) & 0xffffffff, 6)
    d = MD5_STEP(MD5_F4, d, a, b, c, (inputlist[11] + 0xbd3af235) & 0xffffffff, 10)
    c = MD5_STEP(MD5_F4, c, d, a, b, (inputlist[2] + 0x2ad7d2bb) & 0xffffffff, 15)
    b = MD5_STEP(MD5_F4, b, c, d, a, (inputlist[9] + 0xeb86d391) & 0xffffffff, 21)
    digestlist[0] = (digestlist[0] + a) & 0xffffffff
    digestlist[1] = (digestlist[1] + b) & 0xffffffff
    digestlist[2] = (digestlist[2] + c) & 0xffffffff
    digestlist[3] = (digestlist[3] + d) & 0xffffffff
def MD5_MAIN(mes):
    m = fill(mes)
    state = initialState
    for i in range(len(m) // 16):
        last = []
        for j in range(16):
            last.append(m[16*i+j])
        MD5_TRANSFORM(state, last)
    return (state[0].to_bytes(length=4, byteorder='little') + state[1].to_bytes(length=4, byteorder='little') +
            state[2].to_bytes(length=4, byteorder='little') + state[3].to_bytes(length=4, byteorder='little')).hex()
if __name__ == '__main__':
    f4 = open('./MD5.txt',encoding='utf-8')
    content = f4.readline().replace('\n','').replace('\r','')
    sum = 0
    sum_time = 0
    #利用循环全部读出
    while content:
        s = content
        KB=list(bytes(s,'utf-8'))      # 将unicode转换为字节序列
        start_time = time.time()
        temp = MD5_MAIN(KB)
        end_time = time.time()
        print(temp)
        runtime = end_time - start_time
        sum_time = sum_time + runtime
        content = f4.readline().replace('\n', '').replace('\r', '')
        sum = sum + 1
    f4.close()
    print('sum:',sum)
    print('平均用时:',sum_time/sum)
