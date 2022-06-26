class Solution:
    def rob(self, nums):
        n = len(nums)
        if nums == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if (i == 1):
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
