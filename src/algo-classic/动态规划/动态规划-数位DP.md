## 数位DP

**06/04/2023**


### 数位DP的基本思想
> 从高位到低位枚举，每一位填数字。构造数字。

### 数位DP的模板
> 通常使用记忆化搜索的方式实现，根据题目不同，定义的函数参数也不同。通常固定为,dfs(i, is_limit),通常是固定的，i表示当前的位置，is_limit表示是否受限制，即是否有上界。受到上一个数字的限制。
> 其它参数通常根据题意进行定义，比如每一位是否不同，是否有连续的0，是否有连续的6，8，9等等。
> 需要特殊考虑的前导0的问题，如果题目需要去除前导0，可以在dfs函数中加入一个参数，表示是否有前导0，如果有前导0，那么下一位就不能为0，否则可以为0。

- Python
```python
```

### 题目

#### [Q2376] - Count Special Integers - Hard
#### Solution:

- High Level:
  > 统计具有某种性质的数字的个数。使用数位DP的思想，从高位到低位枚举，每一位填数字。构造数字。
  > 构造思想，如何构造数字，一位一位构造数字
  > 从i开始填数字,i前面填的数字的集合是mask,能构造出的特殊整数的数目。
  > is_limit表示前面填的数字是否都是n对应位的，如果为true，那么当前为至多为s[i],否则至多为9
  > is_num，这个是为前导0来考虑的，表示前面是否填了数字(是否跳过)，如果为true，那么当前位可以从0开始，如果为false,那么我们可以跳过，或者可以填1-9。

- Algorithm Knowledge:
  > 数位DP模板的应用。

- Code Tricks:
  > 对于每一位数字是否不同，可以使用一个mask表示不同数字的集合，然后使用mask >> d & 1 判断 d是否在集合中。


#### Code:

- Python
```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return is_num

            res = 0
            if not is_num: # 继续跳过
                res = f(i+1, mask, False, False)
            # 不跳过，构造数字
            up = int(s[i]) if is_limit else 9
            for d in range(1-is_num, up+1):
                if mask >> d & 1 == 0: # mask里面没有d
                    res += f(i+1, mask|(1<<d), is_limit and up == d, True)
            return res 
        
        return f(0, 0, True, False)
```
- Java

```java
```

- Typescript
```typescript
function countSpecialNumbers(n: number): number {
    const s = String(n);
    const cache: Map<string, number> = new Map();

    function f(i: number, mask: number, isLimit: boolean, isNum: boolean): number {
        if (i === s.length) {
            return isNum ? 1 : 0;
        }

        // 记忆化搜索key
        const cacheKey = `${i}-${mask}-${isLimit}-${isNum}`;
        if (cache.has(cacheKey)) {
            return cache.get(cacheKey)!;
        }

        let res = 0;
        if (!isNum) { // 继续跳过
            res = f(i + 1, mask, false, false);
        }

        const up = isLimit ? Number(s[i]) : 9;
        for (let d = 1 - Number(isNum); d <= up; d++) {
            if ((mask >> d & 1) === 0) {
                res += f(i + 1, mask | (1 << d), isLimit && up === d, true);
            }
        }
        // 放入缓存
        cache.set(cacheKey, res);
        return res;
    }

    return f(0, 0, true, false);
}
```

### [Q2] -  

#### Solution:

- High Level:
  > 

- Algorithm Knowledge:
  > 

- Code Tricks:
  > 

#### Code:

```python
```


#### Java

```java
```

#### Related Problems:

- 

## Go
**Go! Grow together**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO -     http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Q2376]: <https://leetcode.cn/problems/count-special-integers/description/>