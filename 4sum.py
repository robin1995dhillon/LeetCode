class Solution(object):
    def fourSum(self, nums, target):
        numlist = []
        nums.sort()
        for i, a in enumerate(nums):
            for p in range(i + 1, len(nums)):
                q = p + 1
                r = len(nums) - 1
                while q < r:
                    sum = a + nums[p] + nums[q] + nums[r]
                    if sum < target:
                        q += 1
                    elif sum > target:
                        r -= 1
                    else:
                        numlist.append([a, nums[p], nums[q], nums[r]])
                        q += 1
        unique_data = [list(x) for x in set(tuple(x) for x in numlist)]
        return unique_data


# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# nums = [2, 2, 2, 2, 2]
# target = 8
nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
s = Solution()
value = s.fourSum(nums, target)
print(value)
