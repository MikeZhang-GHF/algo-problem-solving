### 树形 DP

**08/16/2023**

#### 核心思想

> 思考整棵树和左右子树的关系。
> 原问题: 整棵树
> 子问题: 左右子树
> 常见的套路: 1. 选/不选 2. 选哪个
> 适用的场景，维护树上一些信息。树的结构，天然适合使用递归，DP 维护的就是子问题中的信息，如极值等，因为很多问题可以看做根节点，左右子树的问题，左右子树同时是原来问题的子问题。更新信息分为两个方向，多数是子树向父节点更新，直到根节点。少数是父节点 pushdown 一些信息，来更新子树的信息。

#### 代码模板

> 1. 建图一般使用邻接表，无向图。使用数组来建图。
> 2. 递归函数，参数一般是当前节点，父节点，返回值一般是当前节点的信息。

```python
  # 1. 建图，无向图，n个节点，n-1条边
  g = [[] for _ in range(n)]]]
  for x, y in edges:
    g[x].append(y)
    g[y].append(x)

  # 2. 递归函数
  def dfs(x: int, fa: int):
    # 递归终止条件
    for y in g[x]:
      if y == fa:
        continue
      dfs(y, x)
      # 维护信息逻辑
    # 返回信息给父节点
    return

  # 3. 调用递归函数
  dfs(0, -1)
```

#### 相关问题

[Q543] - Diameter of Binary Tree

> 整棵树的最大深度 = max(左子树的最大深度，右子树的最大深度) + 1
> 换个角度看路径：从一个叶子节点向上，到某个**子树**拐弯，向下到达另一个叶子。得到了由两条链拼出来的路径。（也可能是一条链）
> 枚举子树的根，**直径** = 左子树的最长链 + 右子树的最长链 + 2
> 返回给父节点的是以**当前节点为根的子树的最长链**=max(左子树的最长链，右子树的最长链) + 1，因为只能选一条链，所以只能选左右子树中最长的那条链，它要和父节点的链拼接起来，所以+1。

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node is None:
                return -1
            left_len = dfs(node.left) + 1 # 叶子节点链长=0
            right_len = dfs(node.right) + 1
            nonlocal ans
            # 更新路径最大值
            ans = max(ans, left_len + right_len)
            return max(left_len, right_len) # 返回给父节点信息

        dfs(root)
        return ans
```

[Q124] - Binary Tree Maximum Path Sum

> 路径相关问题，枚举**拐弯**的位置，来维护路径上点值之和的最大值。
> 当前**拐弯**的最大路径和=左子树最大链和+右子树最大链和+当前节点值
> 返回给父节点信息=max(左子树最大链和, 右子树最大链和) + 当前节点值如果这个数是负数，就不要了，返回 0，因为负数只会拖累路径和。

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if node is None:
                return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_val + r_val + node.val)
            return max(0, max(l_val, r_val) + node.val)

        dfs(root)
        return ans
```

[Q1245] - Tree Diameter

> 分类讨论，树的直径可能在当前的子树中，也可能不在。考虑经过子树根节点的最长路径就好了。
> 子树可以为它的父节点提供最大深度的那个叶子的路径，就是最长链信息，就可以了。本质就是树形 DP。

```python
def get_tree_diameter(edges: List[List[int]]):
    n = len(edges) + 1
    # 邻接表建树，无向图
    g = [[] for _ in range(n)]
    for x, y in edges:
      g[x].append(y)
      g[y].append(x)

    ans = 0
    def dfs(x: int, fa: int):
      nonlocal ans
      max_len = 0 # 以x为根节点的子树的最长链
      for y in g[x]:
        if y == fa:
          continue
        mx = dfs(y, x)
        ans = max(ans, max_len + mx)
        max_len = max(max_len, mx)
      return max_len + 1 # 返回给父节点子数的最长链
    dfs(0, -1)
    return ans
```

[Q2246] - Longest Path With Different Adjacent Characters

> 对于一般的树，不是二叉树的情况，思路相同，枚举**拐弯**的位置，遍历所有邻居，维护最长长度，一定会在遍历某棵子树时算出最大+次大。

```python
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n): # 根节点是0
            g[parent[i]].append(i) # 只有一条边

        ans = 0
        def dfs(x):
            nonlocal ans
            x_len = 0
            for y in g[x]:
                y_len = dfs(y) + 1
                if s[y] != s[x]: # 相邻节点字符不同
                    ans = max(ans, x_len + y_len)
                    x_len = max(x_len, y_len)
            return x_len # 维护最大值
        dfs(0)
        return ans + 1 # 求点的个数需要+1
```

[Q2538] - Difference Between Maximum and Minimum of Tree

> 最小的一条路径只有一个节点，因为所有节点的值都是**正数**
> 开销:一条路径 `-` 一个点
> 最大开销: 路径和越大越好，尽量长 => 两端都是叶子节点，(树的直径 1245)
> 如何去掉一个点后的最大路径和，锻炼分类讨论能力，去掉的都是叶子节点。
>
> 1. 当前完整 + 其它子树去掉一个叶子节点
> 2. 当前链去掉一个节点 + 其它子树完整的链
>
> -   时间复杂度: $`O(n)`$，其中 n 为节点个数。
> -   空间复杂度: $`O(n)`$，其中 n 为节点个数。

```python
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0
        def dfs(x: int, fa: int) -> (int, int):
            nonlocal ans
            # 1. 返回带上端点的最大路径和，去掉端点的最大路径和
            max_s1 = p = price[x] # 带上端点
            max_s2 = 0 # 去掉端点
            for y in g[x]:
                if y == fa:
                    continue
                s1, s2 = dfs(y, x)
                ans = max(ans, s1 + max_s2, s2 + max_s1)
                max_s1 = max(max_s1, s1 + p)
                max_s2 = max(max_s2, s2 + p) # 一定不是叶子节点，一定带上p
            return max_s1, max_s2
        dfs(0, -1)
        return ans
```

[Q337] - House Robber III

> 对于每个节点可以选/不选，两种状态，维护两个状态的最大值。返回给父节点的是两个状态的最大值。
> 选 = 左不选 + 右不选 + 当前节点值， 不选 = max(左选，左不选) + max(右选，右不选)
> 答案 = max(选，不选)
> 本题是 🌲 上最大独立集问题，最大独立集问题是求最大的不相邻节点的和，本题是求最大的相邻节点的和。
> 时间复杂度: $`O(n)`$，其中 n 为节点个数。
> 空间复杂度: $`O(n)`$，其中 n 为节点个数。

```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            # 选当前节点
            rob = l_not_rob + r_not_rob + node.val
            # 不选当前节点
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return rob, not_rob
        return max(dfs(root))
```

[Q2581] - Count Number of Possible Root Nodes

> 换根 DP
> 把以 `0`为根猜对的次数算出来`cnt0` DFS，结果都放在哈希表`s`里，可以`O(1)`查找
> DFS，`0`换成`1`为根猜对的次数的变化量算出来，`cnt - (0,1) in s + (1,0) in s`

```python
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # 1. 建图使用数组，会快一些
        n = len(edges)
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        s = set((x, y) for x, y in guesses) # O(1) lookup

        # 1. 求出初始状态以0为根猜对的次数
        cnt0 = 0
        def dfs(x: int, fa: int) -> None:
            nonlocal cnt0
            for y in g[x]:
                if y == fa:
                    continue
                cnt0 += (x, y) in s
                dfs(y, x)
        dfs(0, -1)

        # 2. 进行换根，来更新答案
        ans = 0
        def reroot(x: int, fa: int, cnt: int) -> None:
            # cnt 表示以x为根时猜对的次数
            nonlocal ans
            if cnt >= k:
                ans += 1
            for y in g[x]:
                if y == fa:
                    continue
                reroot(y, x, cnt - ((x, y) in s) + ((y, x) in s)) # 计算变化量

        reroot(0, -1, cnt0)
        return ans
```

[//]: #
[Q543]: https://leetcode.com/problems/diameter-of-binary-tree/
[Q124]: https://leetcode.com/problems/binary-tree-maximum-path-sum/
[Q337]: https://leetcode.com/problems/house-robber-iii/
[Q2246]: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
[Q1245]: https://leetcode.com/problems/tree-diameter/
[Q2538]: https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/
[Q2581]: https://leetcode.com/problems/count-number-of-possible-root-nodes/
