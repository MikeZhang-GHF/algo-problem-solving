### BFS

**09/22/2023**

#### 01BFS

> 对于边权为 0/1 的图，可以使用 01BFS，时间复杂度$`O(m)`$，空间复杂度$`O(n)`$。使用双端队列，从起点开始，如果当前节点的邻居节点的距离大于当前节点的距离加上边权，那么就更新邻居节点的距离，如果边权为 0，就从队头入队，否则从队尾入队。
> 先拓展近的`k`，然后拓展`k+1`，这样就可以保证最短路。如果每个节点的边权都是 1，那么就是普通的 BFS。可以得到最短路径树。
> `0/1`BFS，`0`代表走的边是横向边。加入队列的头部，`1`代表走的边是竖向边，加入队列的尾部。也是符合队列的二段性。使用双端队列维护入队出队的顺序。
> **拓展**，如果只有两种边权，不是`0`和`1`，比如`2`和`3`，不可以使用上边的做法，因为`3`可能多次入队。
> **拓展**，如果边权是`0`和`x`，可以使用 01BFS，因为使用等比例缩放，即可。

#### 代码模板

```python
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < m and 0 <= ny < n:
                    d = grid[nx][ny]
                    if dist[x][y] + d < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + d
                        if d == 0: # 边权是0，入队头
                            q.appendleft((nx, ny))
                        else: # 边权是1，入队尾
                            q.append((nx, ny))
        return dist[m - 1][n - 1]
```

#### 相关问题

[Q2290] Minimum Obstacle Removal to Reach Corner

> 障碍物的代价是`1`，空格子代价`0`。边权是 0/1，可以使用 01BFS，求最短路。当然也可以使用 Dijkstra 算法，边权都是正数，求最短路。

```python
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < m and 0 <= ny < n:
                    d = grid[nx][ny]
                    if dist[x][y] + d < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + d
                        if d == 0: # 边权是0，入队头
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return dist[m - 1][n - 1]
```

[//]: #
[Q2290]: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
