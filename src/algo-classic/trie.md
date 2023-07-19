### Trie

**07/17/2023**

#### 核心思想
> 适用的场景，主要在线性的数据结构上，利用数据的性质。可以将数据分成两段，具有**二段性**。找到一个性质，就是解决这类问题的关键。
> 二分是常用的算法，如果题目中出现关键字，最大的最小，最小的最大，之类的词语，使用二分算法的可能性非常大。
> 如果没有思路的时候，也可以试试二分。观察数据范围也是非常重要的提示。

#### 代码模板
>

```python
class Node:
    __slots__ = 'son', 'is_word'

    def __init__(self):
        # 儿子节点都是字典，不用数组26来实现
        self.son = defaultdict(Node)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root 
        for c in word:
            cur = cur.son[c]
        cur.is_word = True 

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word:
            if c not in cur.son:
                return False 
            cur = cur.son[c]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.son:
                return False 
            cur = cur.son[c]
        return True 
```

#### 相关问题

[Q208] Implement Trie (Prefix Tree)
> - 关键字，前缀/后缀。Trie特别适合维护很多字符串的前缀或后缀信息
> - 模板题
> - 时间复杂度O(n)
> 


[//]: # 
   [Q208]: <https://leetcode.com/problems/implement-trie-prefix-tree/>
   [Q139]: <https://leetcode.com/problems/word-break/>
   [Q]: <>