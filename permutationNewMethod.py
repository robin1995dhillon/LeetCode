class Solution(object):
    def permute(self, nums):
        answers = []
        val = []

        ans = self.permutation(nums, answers, val)
        return ans

    def permutation(self, nums, answers, val):
        n = len(nums)
        if n == 0:
            answers.append(val.copy())

        for i in range(n):
            popped_value = nums.pop(i)
            val.append(popped_value)
            self.permutation(nums, answers, val)
            val.pop()
            nums.insert(i,popped_value)

        return answers


sol = Solution()
nums = [1, 2, 3]
value = sol.permute(nums)
print(value)
# -1072891183
# 119983488
