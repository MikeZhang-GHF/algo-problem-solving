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
            is_num: 前面的数字是否填过数字(是否跳过)，每一个位置可以**填/跳过**
            is_limit: 前面一个数字是否到达它的范围的上限，true，上界s[i]，false，上界9
                    true，当前可以从0开始，
                    false，1. 可以跳过 2. 可以从1开始填数字
                    default: True
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

[Q2376] - Count Special Integers - Hard
> 统计具有某种性质的数字的个数。使用数位DP的思想，从高位到低位枚举，每一位填数字。构造数字。
> 构造思想，如何构造数字，一位一位构造数字
> 从i开始填数字,i前面填的数字的集合是mask,能构造出的特殊整数的数目。
> is_limit表示前面填的数字是否都是n对应位的，如果为true，那么当前为至多为s[i],否则至多为9
> is_num，这个是为前导0来考虑的，表示前面是否填了数字(是否跳过)，如果为true，那么当前位可以从0开始，如果为false,那么我们可以跳过，或者可以填1-9

- Code Tricks:
> 对于每一位数字是否不同，可以使用一个mask表示不同数字的集合，然后使用mask >> d & 1 判断 d是否在集合中。

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

[Q2801] - Count Stepping Numbers in Range - Hard
> 涉及到每个数字的前后关系，使用数位DP的思想，从高位到低位枚举，每一位填数字。构造数字。
> 有上下界转换成上界问题，变成相减。[0, high] - [0, low - 1]
> 将数字DP模板填数字部分的逻辑改变即可，not is_num or abs(d - pre) == 1

```python
MOD = 10**9 + 7

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        def calc(s: str) -> int:
            @cache 
            def dfs(i: int, pre: int, is_num: bool, is_limit: bool=True) -> int:
                if i == len(s):
                    return int(is_num)

                res = 0
                if not is_num:
                    res = dfs(i + 1, pre, False, False)
                low = 0 if is_num else 1
                up = int(s[i]) if is_limit else 9
                for d in range(low, up + 1):
                    if not is_num or abs(d - pre) == 1: # 第一个数字任意，后面的数字abs=1
                        res += dfs(i + 1, d, True, is_limit and d == up)
                return res 
            return dfs(0, 0, False)
        
        return (calc(high) - calc(str(int(low) - 1))) % MOD
```

[Q2719] - Count of Integers - Hard
> 涉及到每个数字的前后关系，使用数位DP的思想，从高位到低位枚举，每一位填数字。构造数字。
> 有上下界转换成上界问题，变成相减。[0, high] - [0, low - 1]
> 将数字DP模板填数字部分的逻辑改变即可，因为这道题求所有数位的和，不需要考虑前导0的问题，所以is_num可以去掉，low也可以去掉。维护各位数字和即可。

```python
MOD = 10 ** 9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def calc(s: str) -> int:
            @cache
            def dfs(i: int, sum: int, is_limit: bool=True) -> int:
                if sum > max_sum:
                    return 0
                if i == len(s):
                    return sum >= min_sum
                res = 0
                up = int(s[i]) if is_limit else 9
                for d in range(up + 1):
                    res += dfs(i + 1, sum + d, is_limit and d == up)
                return res % MOD
            return dfs(0, 0)
        
        return (calc(num2) - calc(str(int(num1) - 1))) % MOD
```

[Q233] - Number of Digit One - Hard
> 涉及到每个数字的前后关系，使用数位DP的思想，从高位到低位枚举，每一位填数字。构造数字。
> 这里不涉及到前导0的问题，所以不需要is_num。
> 维护逻辑，cnt1表示1的个数。维护1的个数即可。

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        @cache
        def dfs(i, cnt1, is_limit=True):
            if i == len(s):
                return cnt1
            res = 0
            up = int(s[i]) if is_limit else 9 
            for d in range(up + 1):
                res += dfs(i + 1, cnt1 + (d == 1), is_limit and up == d)
            return res 
        return dfs(0, 0)
```

[Q600] - Non-negative Integers without Consecutive Ones - Hard
> 涉及到每个数字的前后关系，使用数位DP的思想，从高位到低位枚举，每一位填数字。构造数字。

```python
class Solution:
    def findIntegers(self, n: int) -> int:
        s = str(bin(n))[2:]
        @cache 
        def dfs(i: int, pre1: bool, is_limit: bool=True) -> int:
            if i == len(s):
                return 1
            up = int(s[i]) if is_limit else 1
            res = dfs(i + 1, False, is_limit and up == 0) # 填0
            if pre1 == False and up == 1:
                res += dfs(i + 1, True, is_limit) # 填1
            return res 
        
        return dfs(0, False)
```

[Q902] - Numbers At Most N Given Digit Set - Hard
>

```python
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        @cache
        def dfs(i, is_num, is_limit=True):
            if i == len(s):
                return is_num
            res = 0
            if not is_num:
                res += dfs(i + 1, False, False) 
            up = s[i] if is_limit else '9'
            for d in digits:
                if d > up:
                    break 
                res += dfs(i + 1, True, is_limit and d == up)
            return res 
        return dfs(0, False)
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO -     http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Q233]: <https://leetcode.com/problems/number-of-digit-one/>
   [Q600]: <https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/>
   [Q902]: <https://leetcode.com/problems/numbers-at-most-n-given-digit-set/>
   [Q2376]: <https://leetcode.com/problems/count-special-integers/>
   [Q2801]: <https://leetcode.com/problems/count-stepping-numbers-in-range/>
   [Q2719]: <https://leetcode.com/problems/count-of-integers/>