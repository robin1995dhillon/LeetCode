def moveZeroes(nums):
    j = 0
    n = len(nums)
    for num in nums:
        if num != 0:
            nums[j] = num
            j+=1
    for val in range(j,n):
        nums[val] = 0
    return nums


nums = [2,5,0,6,0,8,7]
print(moveZeroes(nums))