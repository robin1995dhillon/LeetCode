import sys


class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) <= 1:
            return nums
        minimum = sys.maxsize
        i = len(nums) - 1

        pointer = len(nums) - 2
        while (nums[pointer] >= nums[pointer + 1]):
            pointer -= 1
            if pointer == -1:
                new_list = sorted(nums)
                return new_list
        while (i > pointer):
            if (nums[i] > nums[pointer]):
                break
            else:
                i-=1

        temp = nums[i]
        nums[i] = nums[pointer]
        nums[pointer] = temp

        nums[pointer+1:] = reversed(nums[pointer+1:])
        return nums


sol = Solution()
list_1 = [1,4,9,2,3]
value = sol.nextPermutation(list_1)
print(value)
