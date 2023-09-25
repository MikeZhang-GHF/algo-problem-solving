### BFS

**09/22/2023**

#### 01BFS

> 对于边权为 0/1 的图，可以使用 01BFS，时间复杂度$`O(m)`$，空间复杂度$`O(n)`$。使用双端队列，从起点开始，如果当前节点的邻居节点的距离大于当前节点的距离加上边权，那么就更新邻居节点的距离，如果边权为 0，就从队头入队，否则从队尾入队。

#### 代码模板

#### 相关问题

[Q2290] Minimum Obstacle Removal to Reach Corner

> 障碍物的代价是`1`，空格子代价`0`。边权是 0/1，可以使用 01BFS，求最短路。当然也可以使用 Dijkstra 算法，边权都是正数，求最短路。

```python

```

[//]: #
[Q2290]: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
