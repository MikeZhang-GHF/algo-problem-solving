

```python
# KMP 算法下标从1开始，next[1]永远为0
s = 'leetcode'
t = 'leeto'
m, n = len(t), len(s)
t = ' ' + t
s = ' ' + s
next = [0] * (m + 1)
j = 0
for i in range(2, m + 1): # i从2开始，表示错位对齐，因为t需要非前缀对齐
    while j > 0 and t[i] != t[j + 1]:
        j = next[j]
    if t[i] == t[j + 1]:
        j += 1
    next[i] = j 

j = 0
for i in range(1, n + 1): # i从1开始，s和t头部对齐是有意义的
    while j > 0 and (j == m or s[i] != t[j + 1]): # 找到所有的匹配
        j = next[j]
    if s[i] == t[j + 1]:
        j += 1
    if j == m: # t在s中第一次出现
        ans.append(i - m)
```

[Q28] - Find the Index of First Occurrence in a String

```python
class Solution:
    def strStr(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        s = ' ' + s
        t = ' ' + t 
        next = [0] * (m + 1)
        j = 0
        for i in range(2, m + 1): # t串错位匹配，下标从2开始
            while j > 0 and t[i] != t[j + 1]:
                j = next[j]
            if t[i] == t[j + 1]:
                j += 1
            next[i] = j
        
        j = 0
        for i in range(1, n + 1): # s和t匹配可以从头开始，下标从1开始
            while j > 0 and s[i] != t[j + 1]:
                j = next[j]
            if j < m and s[i] == t[j + 1]:
                j += 1
            if j == m:
                return i - m
        return -1
```


[//]: # 

[Q28]: <https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/>