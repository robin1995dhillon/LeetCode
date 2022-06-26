import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        final_sum = 0
        maximum = sys.maxsize
        nums.sort()
        for i, a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum == target:
                    return target
                elif sum < target:
                    l += 1
                else:
                    r -= 1
                val = abs(target - sum)
                # print(val)
                if (val < maximum):
                    maximum = val
                    final_sum = sum


        return final_sum




# nums = [1,2,4,8,16,32,64,128]
# target = 82

# nums = [-1,2,1,-4]
# target = 1

nums = [1,1,1,0]
target = -100
s = Solution()
value = s.threeSumClosest(nums, target)
print(value)