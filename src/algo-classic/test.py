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


# s, t = 'sadbutsad', 'sad'
# print(strStr(s, t))


def nextPermutation(nums) -> None:
    n = len(nums)
    i = n - 2
    # 从后往前找到第一个不满足递减的数
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        # 从后往前找到第一个比nums[i]大的数，就是下一个排列
        j = n - 1
        while i < j and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    # 保持递增
    nums[i+1:] = reversed(nums[i+1:])

nums = [1, 2, 3, 4, 5, 6]
for _ in range(len(nums)):
    nextPermutation(nums)
    print(nums)

from itertools import permutations

nums = [1, 2, 3, 4, 5, 6]
for _ in range(len(nums)):
    nums = next(permutations(nums))
    print(nums)

x = 10
print(2 << x.bit_length())


import difflib

old_text = "Hello world!\nThis is the old text.\n"
new_text = "Hello world!\nThis is the new text.\n"

diff = difflib.unified_diff(old_text.splitlines(keepends=True), new_text.splitlines(keepends=True))
print(''.join(diff))
