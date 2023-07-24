N = 100010 
P, M = 131, (1 << 64) - 1

h, p = [0] * N, [0] * N
p[0] = 1

# 下标都从1开始
def get_sub_hash(l, r):
    return (h[r] - h[l - 1] * p[r - l + 1]) % M

def preprocess(s): 
    for i in range(1, len(s) + 1):
        h[i] = (h[i-1] * P + ord(s[i - 1])) % M
        p[i] = (p[i-1] * P) % M

def get_hash(s):
    hash_value = 0
    for c in s:
        hash_value = (hash_value * P + ord(c)) % M
    return hash_value

ans = []
def strStr(s: str, t: str) -> int:
    n, m = len(s), len(t)
    preprocess(s)
    hash_t = get_hash(t)
    for i in range(1, n - m + 2):
        if get_sub_hash(i, i + m - 1) == hash_t:
            ans.append(i - 1)
    return ans if len(ans) else -1

s, t = 'sadbutsad', 'sad'
print(strStr(s, t))
        