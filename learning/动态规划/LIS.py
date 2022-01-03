from typing import List
# 最长递增子序列（Longest Increasing Subsequence)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示以nums[i]结尾的数的最大子串长度
        dp = []
        for _ in range(len(nums)):
            dp.append(1)
        for x in range(len(nums)):
            for y in range(x+1):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        res = 0
        for x in dp:
            res = max(res, x)
        return res


nums = [1, 2, 7, 4, 3, 0, 8, 9]
print(Solution().lengthOfLIS(nums))
