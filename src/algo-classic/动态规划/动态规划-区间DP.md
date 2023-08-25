### 区间 DP

**08/25/2023**

#### 核心思想

> 适用的场景，线性 DP，一般都是在前缀/后缀上转移，**区间 DP**，从小区间转移到大区间。
> 思考的方法，1 选/不选 从两侧向内**缩小**问题规模 2 选哪个，**分割**成多个规模更小的子问题

#### 代码模板

> 可以先写记忆化搜索，然后改成递推。如果是多维状态，注意循环的次序，正序还是倒序，取决于状态转移的次序。

#### 相关问题

[Q516] Longest Palindromic Subsequence

> 方法一，转化成最长公共子序列问题，反转后`s`和 s 的 LCS
> 方法二，序列问题，可以使用选或不选。对于区间的两侧，可以选择，也可以不选择，然后缩小问题规模。从两侧向内缩小问题规模。
> 左右端点相等，都选（同最长公共子序列的证明）。左右端点不等，选左端点，或者选右端点，取决于哪个能够使得子问题的规模更小。

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i, j - 1), dfs(i + 1, j))
        return dfs(0, n - 1)
```

```python
f = [[0] * n for _ in range(n)]
for i in range(n - 1, -1, -1): # i逆序
    f[i][i] = 1
    for j in range(i + 1, n): # j正序
        if s[i] == s[j]:
            f[i][j] = f[i+1][j-1] + 2
        else:
            f[i][j] = max(f[i+1][j], f[i][j-1])
return f[0][n - 1]
```

[Q1039] Minimum Score Triangulation of Polygon

> 寻找子问题，开始区间的两侧端点一定在答案中，枚举最后一个三角形的顶点，然后缩小问题规模。
> `v[i,j]`定义成从 i 到 j 顺时针方向的多边形的最小分数，`v[i,j] = min(v[i,k] + v[k,j] + A[i] * A[j] * A[k])`，`k`是`i`和`j`之间的点。
> 递归边界，只有 2 个点，`v[i,j] = 0`。

```python
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dfs(i:int, j:int) -> int:
            if j == i + 1:
                return 0

            res = inf
            for k in range(i + 1, j): # 枚举选哪个点作为最后一个三角形的顶点，分成两个子问题
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
            return res
        return dfs(0, n - 1)
```

```python
f = [[0] * n for _ in range(n)]
# 注意循环顺序
# f[i][j] = min(f[i][k], f[k][j] + v[i]*v[j]*v[k])
# i < k, f[i]从f[k]转移过来，倒序枚举
# j > k, f[i][j] 从f[i][k]转移过来，正序枚举
for i in range(n - 3, -1, -1): # i倒序枚举 j至少从i+2开始，后面有2个点
    for j in range(i + 2, n): # j正序枚举
        res = inf
        for k in range(i + 1, j):
            res = min(res, f[i][k] + f[k][j] + values[i] * values[j] * values[k])
        f[i][j] = res
return f[0][n - 1]
```

[//]: #
[Q516]: https://leetcode.com/problems/longest-palindromic-subsequence/
[Q1039]: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
