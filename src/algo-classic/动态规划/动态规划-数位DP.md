## 数位DP

**06/04/2023**


### 数位DP的基本思想
> 从高位到低位枚举，每一位填数字。构造数字。

### 数位DP的模板
> 通常使用记忆化搜索的方式实现，根据题目不同，定义的函数参数也不同。基础dfs(i, is_limit),通常是固定的，i表示当前要填数字的位置，is_limit表示是否受限制，即是否有上界。受到上一个数字的限制。
> 1. 上一位数字没有到限制，那么当前位可以填的数字，[0,9]
> 2. 上一位数字到达限制，那么当前位可以填的数字，[0, s[i]],s[i]表示n的第i位数字。
> 
> 递归函数，其它参数通常根据题意进行定义，比如每一位是否不同，是否有连续的0，是否有连续的6，8，9等等。
> 需要特殊考虑的**前导0**的问题，如果题目需要去除前导0，可以在dfs函数中加入一个参数，表示是否有前导0，如果有前导0，那么下一位就不能为0，否则可以为0。
> 综上所述，dfs函数的参数定义，
>  - i, is_limit, 为基础参数，表示当前要填数字的位置，是否受限制
>  - x, 根据题意需要维护的参数，比如维护前面已经填写数字的集合等等
> - is_num, 处理前导零问题，表示前面是否填了数字(是否跳过)，如果为true，那么当前位可以从0开始，如果为false,那么当前要填数字2种情况，我们可以跳过，或者可以填1-9。 

- Python
```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache
        def dfs(i: int, mask: int, is_num: bool, is_limit=True) -> int:
            """
            
            Keyword arguments:
            i: 当前要填数字的位置
            mask: 前面填的数字的集合
            is_limit: 前面一个数字是否到达它的范围的上限，true，上界s[i]，false，上界9
            is_num: 前面的数字是否填过数字(是否跳过)，每一个位置可以**填/跳过**
                    true，当前可以从0开始，
                    false，1. 可以跳过 2. 可以从1开始填数字
            Return: 满足限制的数字的个数
            """

            if i == len(s):
                return <需要维护的信息>
            
            res = 0
            if is_num == False: # 前面没有填过数字
                res = dfs(i + 1, mask, False, False) # 跳过
            # 不跳过，填数字    
            upper_bound = int(s[i]) if is_limit else 9
            for d in range(1 - is_num, upper_bound + 1):
                if mask >> d & 1 == 0: # 判断d是否已经填过
                    res += dfs(i + 1, <维护状态>, True, is_limit and (d == upper_bound))
            return res 
        return dfs(0, 0, False) # is_limit初始化为True，否则后面的数字随便填，开始需要约束   
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
        def dfs(i: int, is_limit: bool, mask: int, is_num: bool) -> int:
            """
            
            Keyword arguments:
            i: 当前要填数字的位置
            mask: 前面填的数字的集合
            is_limit: 前面一个数字是否到达它的范围的上限，true，上界s[i]，false，上界9
            is_num: 前面的数字是否填过数字(是否跳过)，
                    true，当前可以从0开始，
                    false，1. 可以跳过 2. 可以从1开始填数字
            Return: 满足限制的数字的个数
            """

            if i == len(s):
                return int(is_num)
            
            res = 0
            if is_num == False: # 前面没有填过数字
                res = dfs(i + 1, False, mask, False) # 跳过
            # 不跳过，填数字    
            upper_bound = int(s[i]) if is_limit else 9
            for d in range(1 - is_num, upper_bound + 1):
                if mask >> d & 1 == 0: # 判断d是否已经填过
                    res += dfs(i + 1, is_limit and (d == upper_bound), mask|(1<<d), True)
            return res 
        return dfs(0, True, 0, False) # is_limit初始化为True，否则后面的数字随便填，开始需要约束，固定
```
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