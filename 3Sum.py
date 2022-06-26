class Solution(object):
    def threeSum(self, nums):
        val_list = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    val_list.append([a, nums[l], nums[r]])
                    r-= 1 # u can update l+=1 as well (check your leetcode)
                    while nums[r] == nums[r+ 1] and l < r:
                        r-= 1
                        
        # return val_list
        print(val_list)


# nums = [3, -2, 1, 0]
s = Solution()
# nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
nums = [-2,0,0,2,2]
val = s.threeSum(nums)
