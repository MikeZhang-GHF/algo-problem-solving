## 思维题

**06/01/2023**

### [Q6472] -  查询后矩阵的和 - Medium

#### Solution:

- High Level:
  > 直接暴力模拟会超时，注意到一个性质，后面的的操作会覆盖到前面的操作，所以可以倒序枚举操作。模拟的过程中，对于行操作，需要知道哪些列没有被操作过，对于列操作，需要知道哪些行没有被操作过。需要维护两个哈希表来维护这些信息。

- Algorithm Knowledge:
  > 倒序枚举，哈希表

- Code Tricks:
  > 只有两个哈希表，互相访问使用 x^1可以得到另一个哈希表。

#### Code:
- Python

```python
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0
        vis = [set(), set()]
        for tp, index, val in reversed(queries):
            if index not in vis[tp]:
                ans += val * (n - len(vis[tp^1]))
                vis[tp].add(index)
        return ans
```

- Java
```java

```

- Typescript
```typescript
function matrixSumQueries(n: number, queries: number[][]): number {
    let ans = 0;
    const vis: Set<number>[] = [new Set(), new Set()];

    for (let i = queries.length - 1; i >= 0; i--) {
        const [tp, index, val] = queries[i];
        
        if (!vis[tp].has(index)) {
            ans += val * (n - vis[tp ^ 1].size);
            vis[tp].add(index);
        }
    }
    return ans;
};
```

#### Related Problems:

- 

## Go
**Go! Grow together**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO -     http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Q6472]: <https://leetcode.cn/problems/sum-of-matrix-after-queries/description/>