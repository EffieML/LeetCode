
def uncompress(s):
    s2 = ''
    for i in range(0, len(s), 2):
        n = int(s[i])
        c = s[i+1]
        for j in range(n):
            s2 += c
    return s2


print(uncompress("2c3a1t"))
