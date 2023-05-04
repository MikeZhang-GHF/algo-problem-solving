## Algorithm Problem Solving Workout
**05/04/2023**
### Q1: Get all numbers from a string
>-input: a string, could be **null**
>-output: a list of numbers(string)
>come at least two methods to solve this problem.
#### Solution:
>- High Level:
>  
>- Algorithm Knowledge:
>
>- Code Tricks:
>
#### Code:
```python

```

```java

```

### [[Q2]] -  Shortest Cycle in a Graph
#### Solution:
>- High Level:
>  
>- Algorithm Knowledge:
>
>- Code Tricks:
>
#### Code:
##### python
```Python
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        def bfs(start: int) -> int:
            ans = inf
            dis = [-1] * n  # dis[i] 表示从 start 到 i 的最短路长度
            dis[start] = 0
            q = deque([(start, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:  # 第一次遇到
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:  # 第二次遇到
                        ans = min(ans, dis[x] + dis[y] + 1)
            return ans

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1
```
##### Java
```java
class Solution {
    private List<Integer>[] g;
    private int[] dis;

    public int findShortestCycle(int n, int[][] edges) {
        // build the graph
        g = new ArrayList[n]; // new int[n]
        Arrays.setAll(g, e -> new ArrayList<Integer>());
        for(var e: edges) {
            int x = e[0], y = e[1];
            g[x].add(y);
            g[y].add(x);
        }
        dis = new int[n];
        int ans = Integer.MAX_VALUE;
        // enumerate each node as start point
        for (int i = 0; i < n; ++i) 
            ans = Math.min(ans, bfs(i));
        return ans < Integer.MAX_VALUE ? ans : -1;
    }

    private int bfs(int start) {
        int ans = Integer.MAX_VALUE;
        Arrays.fill(dis, -1);
        // 记住father
        var q = new ArrayDeque<int[]>();
        q.add(new int[]{start, -1});
        dis[start] = 0;

        while (!q.isEmpty()) {
            var p = q.poll();
            int x = p[0], fa = p[1];
            for (var y: g[x]) {
                if (dis[y] < 0) {
                    dis[y] = dis[x] + 1;
                    q.add(new int[]{y, x});
                } else if (y != fa) {
                    ans = Math.min(ans, dis[x] + dis[y] + 1);
                }
            }
        }
        return ans;
    }
}
```


## Go
**Go! Grow together**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO -     http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Q2]: <https://leetcode.cn/problems/shortest-cycle-in-a-graph/>