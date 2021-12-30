# 给定固定面额的硬币，以最少的数量凑出给定金额
# 0 = 0
# 1 = 1
# 2 = 1 + 1 ...

# 1.base case: amount为0的时候无需计算直接返回
# 2.状态：原问题和子问题中会变化的变量，此时唯一的状态就是目标金额amount
# 3.选择：导致状态变化的行为。每选择一枚硬币， 目标金额的数量就会减少相应的数量，所以所有硬币的面值，就是选择。
# 4.dp数组的定义：一般来说函数的参数就是要求计算的量，即上面的状态。函数的返回值就是题目要求计算的量。
# dp(n)的定义：输入一个目标金额n, 返回凑出该金额n的最少硬币数量


# 1.列出子问题，在子问题中选择最优解然后加一
# 时间复杂度O(n**k)
from datetime import datetime


def get_amount01(amount, co):
    if amount < 0:
        return -1
    elif amount == 0:
        return 0
    else:
        res = 10000
        for x in co:
            subproblem = get_amount01(amount - x, co)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            res = min(res, subproblem + 1)
        return res


# 2.带备忘录的递归
# 时间复杂度O(n)
def get_amount02(amount, coins):
    mem = []
    for x in range(amount + 1):
        mem.append(-2)
    return dp(amount, coins, mem)


def dp(amount, coins, mem):
    # print(mem)
    if amount < 0:
        return -1
    elif amount == 0:
        return 0
    if mem[amount] != -2:
        return mem[amount]
    res = 10000
    for x in coins:
        subproblem = dp(amount - x, coins, mem)
        # 子问题无解，跳过
        if subproblem == -1:
            continue
        res = min(res, subproblem + 1)
    mem[amount] = res
    return res


# 3.dp数组的迭代解法
# 当目标金额为n时，需要dp[n]枚硬币
def get_amount03(amount, coins):
    dp = [0]
    for x in range(1, amount + 1):
        # 初始化为n+1
        dp.append(amount + 1)
    for i in range(amount + 1):
        for x in coins:
            sub = i - x
            if sub < 0:
                continue
            dp[i] = min(dp[i], dp[sub] + 1)
    return dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 3, 5]
    # print(get_amount02(0, coins))
    s = datetime.now()
    for x in range(19):
        # print('凑出{}需要最少{}枚硬币'.format(x, get_amount01(x, coins)))
        # print('凑出{}需要最少{}枚硬币'.format(x, get_amount02(x, coins)))
        print('凑出{}需要最少{}枚硬币'.format(x, get_amount03(x, coins)))
    total = datetime.now() - s
    print('花费了{:.2f}ms'.format(total.microseconds))
