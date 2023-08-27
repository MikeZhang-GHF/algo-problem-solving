from functools import cache


def countSpecialNumbers(n: str) -> int:
    s = n

    @cache
    def dfs(i: int, prev: int, is_num: bool, is_limit: bool = True) -> int:
        if i == len(s):
            return is_num

        res = 0
        if not is_num:  # 前面没有填过数字
            res = dfs(i + 1, prev, False, False)  # 跳过
        # 不跳过，填数字
        up = int(s[i]) if is_limit else 9
        low = 0 if is_num else 1
        for d in range(low, up + 1):
            if abs(d - prev) >= 2:
                res += dfs(i + 1, d, True, is_limit and d == up)
        return res
    return dfs(0, 0, False)  # is_limit初始化为True，否则后面的数字随便填，开始需要约束，固定


a, b = '1', '1000000'
print(countSpecialNumbers(b) - countSpecialNumbers(str(int(a) - 1)))
