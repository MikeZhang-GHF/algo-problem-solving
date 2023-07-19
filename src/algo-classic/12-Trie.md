### Trie

**07/17/2023**

#### 核心思想
> 是用空间换时间的数据结构。主要应用场景用于
>  - 处理共同前缀，统计，排序，和保存大量字符串。用于字符串检索，**字符串最长公共前缀，前缀匹配**。
>  - **01字典**，用于处理异或最值问题。
> 优点:利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希表高。节省存储空间，公共前缀共享同样的前缀。
> 三个重要的性质:
>  - 根节点不包含任何字符，字符存在边上。
>  - 从根节点到某个节点，经过的路径就是字符串。
>  - 每个节点的孩子都不同，对应单词和字符是唯一的。

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

```python
class Node:
    __slot__ = 'son', 'is_word'

    def __init__(self):
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

[Q676] Implement Magic Dictionary
> - 关键字，改变一个字符，在字符串集合中查找字符串，本质上是查找字符串个数。并且多次询问。Trie非常擅长处理词频统计。
> - 本质上，是在Trie树上统计一些信息，统计的就是改变一个字符的情况下，是否有一个字符串可以匹配。在树上做dfs即可。
> - 时间复杂度: O($C^L$)
> - 空间复杂度: O($N \times L \times C$) $N = 100$ 存入Trie最多个数，$L = 100$存入字符串的最大长度，$C = 26$为字符集大小。

```python
class Node:
    __slot__ = 'son', 'is_word'

    def __init__(self):
        self.son = defaultdict(Node)
        self.is_word = False


class MagicDictionary:

    def __init__(self):
        self.root = Node()

    
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.son[c]
        cur.is_word = True 
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insert(word)
        

    def search(self, searchWord: str) -> bool:
        def dfs(s, node, i, cnt):
            if node.is_word and i == len(s) and cnt == 1:
                return True
            
            if i == len(s) or cnt > 1:
                return False

            for c in node.son.keys():
                if dfs(s, node.son[c], i + 1, cnt + (c != s[i])):
                    return True 
            return False

        return dfs(searchWord, self.root, 0, 0)
```

[//]: # 
   [Q208]: <https://leetcode.com/problems/implement-trie-prefix-tree/>
   [Q139]: <https://leetcode.com/problems/word-break/>
   [Q676]: <https://leetcode.com/problems/implement-magic-dictionary/description/>