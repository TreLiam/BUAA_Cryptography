# from pycallgraph import Config
# from pycallgraph import PyCallGraph
# from pycallgraph import GlobbingFilter
# from pycallgraph.output import GraphvizOutput
import math
import sys

IP_table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
            ]
# 初始IP置换
_IP_invert = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25
              ]
# 逆初始置换
# S盒中的S1盒
S0 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
      ]
# S盒中的S2盒
S1 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
      ]
# S盒中的S3盒
S2 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
      ]
# S盒中的S4盒
S3 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
      ]
# S盒中的S5盒
S4 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
      ]
# S盒中的S6盒
S5 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
      ]
# S盒中的S7盒
S6 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
      ]
# S盒中的S8盒
S7 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
      ]
S = [S0, S1, S2, S3, S4, S5, S6, S7]

# 拓展置换E盒
Extend_table = [32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9,
                8, 9, 10, 11, 12, 13,
                12, 13, 14, 15, 16, 17,
                16, 17, 18, 19, 20, 21,
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1
                ]
# 线性置换P盒
P_table = [16, 7, 20, 21,
           29, 12, 28, 17,
           1, 15, 23, 26,
           5, 18, 31, 10,
           2, 8, 24, 14,
           32, 27, 3, 9,
           19, 13, 30, 6,
           22, 11, 4, 25
           ]
# 子密钥压缩置换表PC-1
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
        ]
# 子密钥置换选择PC-2
PC_2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
        ]
# 循环移位
moveNum = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def tobin(n):
    s = [0, 0, 0, 0]
    for i in range(4):
        if n % 2 == 0:
            s[i] = 0
        else:
            s[i] = 1
        n = math.floor(n / 2)

    return s[3], s[2], s[1], s[0]


def toBin(Ss):
    # s = [0 for x in range(64)]
    # for i in range(len(Ss)):
    #     s[4 * i], s[4 * i + 1], s[4 * i + 2], s[4 * i + 3] = tobin(int(Ss[i], 16))
    Snum = int("0x" + Ss, 16)
    Sbin = list(map(int, bin(Snum)[2:].zfill(64)))

    return Sbin


def IP(St):
    s = [0 for i in range(len(St))]
    for i in range(len(St)):
        s[i] = St[IP_table[i] - 1]
    return s


def IPinvert(S):
    res = [0 for x in range(len(S))]
    for i in range(len(S)):
        res[i] = S[_IP_invert[i] - 1]
    return res


def leftmove(S, n):
    S[0:len(S) - n], S[len(S) - n:] = S[n:], S[0:n]
    return S


def get_Key(Key):
    # 去掉奇偶校验位
    Key1 = [0 for x in range(len(Key))]
    C = [([0] * 28) for i in range(17)]
    D = [([0] * 32) for i in range(17)]
    roundKey = [([0] * 48) for i in range(16)]
    for i in range(56):
        Key1[i] = Key[PC_1[i] - 1]
    C[0] = Key1[0:28]
    D[0] = Key1[28:56]
    for i in range(1, 17):
        C[i] = leftmove(C[i - 1], moveNum[i - 1])
        D[i] = leftmove(D[i - 1], moveNum[i - 1])
        for j in range(48):
            if PC_2[j] <= 28:
                roundKey[i - 1][j] = C[i][PC_2[j] - 1]
            else:
                roundKey[i - 1][j] = D[i][PC_2[j] - 1 - 28]
    return roundKey


def E_change(R):
    R1 = [0 for i in range(48)]
    for i in range(48):
        R1[i] = R[Extend_table[i] - 1]
    return R1


def s_box(R_extend):
    R1 = [0 for i in range(32)]

    lengh = 0
    for i in range(0, len(R_extend), 6):
        j = R_extend[i] * 2 + R_extend[i + 5]
        k = R_extend[i + 1] * 8 + R_extend[i + 2] * 4 + R_extend[i + 3] * 2 + R_extend[i + 4]
        R1[lengh], R1[lengh + 1], R1[lengh + 2], R1[lengh + 3] = tobin(S[i // 6][j][k])
        lengh = lengh + 4

    return R1


def p_box(R1):
    res = [0 for i in range(len(R1))]
    for i in range(len(R1)):
        res[i] = R1[P_table[i] - 1]
    return res


def F(R, roundKey):
    R_extend = [0 for i in range(48)]
    R1 = [0 for i in range(32)]
    # E盒变换
    R_extend = E_change(R)
    # 异或运算
    for i in range(48):
        R_extend[i] = R[Extend_table[i] - 1] ^ roundKey[i]
    # S盒变换
    R1 = s_box(R_extend)
    # P盒置换
    R1 = p_box(R1)
    return R1


def xor(L, R):
    # assert len(L) == len(R)
    RES = [0 for i in range(len(R))]
    # RES = []
    for i in range(len(R)):
        RES[i]=(L[i] ^ R[i])
    return RES


def encrypt(St, Key):
    # 初始置换
    St = IP(St)
    L = [([0] * 32) for i in range(17)]
    R = [([0] * 32) for i in range(17)]
    res = [0 for x in range(64)]
    L[0] = St[0:32]
    R[0] = St[32:64]
    roundKey = get_Key(Key)
    for i in range(1, 17):
        L[i] = R[i - 1]
        f = F(R[i - 1], roundKey[i - 1])
        R[i] = xor(L[i - 1], f)
    res[0:32], res[32:64] = R[16], L[16]
    # 逆初始置换
    res = IPinvert(res)
    return res


def decrypt(St, Key):
    # 初始置换
    St = IP(St)
    L = [([0] * 32) for i in range(17)]
    R = [([0] * 32) for i in range(17)]
    res = [0 for x in range(64)]
    L[16] = St[0:32]
    R[16] = St[32:64]
    roundKey = get_Key(Key)
    for i in range(1, 17)[::-1]:
        L[i - 1] = R[i]
        f = F(R[i], roundKey[i - 1])
        R[i - 1] = xor(L[i], f)
    res[0:32], res[32:64] = R[0], L[0]
    # 逆初始置换
    res = IPinvert(res)
    return res


def toHex(r_bin):
    res = ""
    for i in range(0, len(r_bin), 4):
        m = r_bin[i] * 8 + r_bin[i + 1] * 4 + r_bin[i + 2] * 2 + r_bin[i + 3]
        res = res + hex(m)[2:]
    return res


def encrypt_three(plaintext, Key1, Key2):
    temp1 = encrypt(plaintext, Key1)
    temp2 = decrypt(temp1, Key2)
    result = encrypt(temp2, Key1)
    return result


def decrypt_three(ciphertxt, Key1, Key2):
    temp1 = decrypt(ciphertxt, Key1)
    temp2 = encrypt(temp1, Key2)
    result = decrypt(temp2, Key1)
    return result


if __name__ == "__main__":
    # Ss = input().strip().replace('\n', '').replace('\r', '')
    # K1 = input().strip().replace('\n', '').replace('\r', '')
    # K2 = input().strip().replace('\n', '').replace('\r', '')
    # flag = int(input())
    # St = toBin(Ss[2:])
    # Key1 = toBin(K1[2:])
    # Key2 = toBin(K2[2:])
    # if flag == 1:
    #     res_bin = encrypt_three(St, Key1, Key2)
    # else:
    #     res_bin = decrypt_three(St, Key1, Key2)
    # res_Hex = toHex(res_bin)
    # print('0x', end='')
    # print(res_Hex, end='')

    K1 = input().strip().replace('\n', '').replace('\r', '')
    K2 = input().strip().replace('\n', '').replace('\r', '')
    IV = input().strip().replace('\n', '').replace('\r', '')
    flag = int(input())
    Ss = input().strip().replace('\n', '').replace('\r', '')
    if Ss.find("0x") != -1:
        Ss = Ss[:-18]
    # print(Ss)
    Key1 = toBin(K1[2:])
    Key2 = toBin(K2[2:])
    IV = toBin(IV[2:])

    if flag == 1:
        if len(Ss) % 16 != 0:
            paddingnum = "0" + hex((16 - len(Ss) % 16) // 2)[2:]
            Ss += paddingnum * int('0x' + paddingnum, 16)
        else:
            paddingnum = "10"
            Ss += 8 * paddingnum
        # CBCblocks = [Ss[i:i + 16] for i in range(0, len(Ss), 16)]
        CBCblocks = []
        for i in range(0, len(Ss), 16):
            CBCblocks.append(Ss[i:i + 16])
        res = []
        for i in range(len(CBCblocks)):
            St = toBin(CBCblocks[i])
            inputmes = xor(St, IV)
            res_bin = encrypt_three(inputmes, Key1, Key2)
            res.append(toHex(res_bin))
            IV = res_bin
        for i in res:
            print(i, end="")
        del Ss
    else:
        CBCblocks = []
        print(Ss)
        for i in range(0, len(Ss), 16):
            CBCblocks.append(Ss[i:i + 16])
            print(i)
        print(CBCblocks)
        res = []
        for i in range(len(CBCblocks)):
            St = toBin(CBCblocks[i][0])
            res_bin = decrypt_three(St, Key1, Key2)
            outputmes = xor(IV, res_bin)
            res.append(toHex(outputmes))
            IV = St
        # paddingnum = int(res[-1][-2:])
        # res[-1] = res[-1][:-paddingnum * 2]
        for i in res:
            print(i, end="")
