# 斐波那契
# f(1) = f(2) = 1
# f(n) = f(n-1) + f(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13

# 1.直接调用，简洁
# O(2**n)
def fib_01(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_01(n - 1) + fib_01(n - 2)


# 2.将冗余的递归树剪枝，如果重复出现直接取出，无需重复计算
# O(n)
def fib_02(n):
    mem = []
    for x in range(n + 1):
        mem.append(0)
    return helper(mem, n)


def helper(mem, n):
    if n == 0 or n == 1:
        return n
    elif mem[n] != 0:
        return mem[n]
    else:
        mem[n] = helper(mem, n - 1) + helper(mem, n - 2)
        return mem[n]


# 3.以上为自顶向下的递归解法，逐渐分解，直至base case.
# 动态规划从最小的问题开始推算，直至想要的结果，为自底向上，由循环迭代完成
# 需要长度为n的list, 空间复杂度O(n)
def fib_03(n):
    # base case
    dp = [0, 1]
    # 状态转移
    for x in range(2, n + 1):
        dp.append(dp[x - 1] + dp[x - 2])
    return dp[n]


# 4.根据状态转移方程可以看出，无需保存n个结果，只需保留前两项即可
# 用状态压缩将dp table的大小从n压缩到2，空间复杂度为O(1)
def fib_04(n):
    pre = 0
    cur = 1
    if n == 0 or n == 1:
        return n
    for x in range(2, n + 1):
        sum = pre + cur
        pre = cur
        cur = sum
    return cur

#leetcode
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    # range(start, stop[, step]) , 左闭右开
    c = Solution()
    for i in range(10):
        # print('fib({})的值是{:^5d}'.format(i, fib_01(i)))
        # print('fib({})的值是{:^5d}'.format(i, fib_02(i)))
        # print('fib({})的值是{:^5d}'.format(i, fib_03(i)))
        # print('fib({})的值是{:^5d}'.format(i, fib_04(i)))
        print('fib({})的值是{:^5d}'.format(i, c.fib(i)))
