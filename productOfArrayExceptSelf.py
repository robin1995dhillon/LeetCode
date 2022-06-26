class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        products = [1] * length
        leftProduct = 1
        for i in range(length):
            products[i] = leftProduct
            leftProduct *= nums[i]
        rightProduct = 1
        for i in reversed(range(length)):
            products[i] *= rightProduct
            rightProduct *= nums[i]
        return products





s = Solution()
nums = [1,2,3,4]
ans = s.productExceptSelf(nums)
print(ans)