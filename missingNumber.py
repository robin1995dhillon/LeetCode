def missingNumber(nums):
    actual_sum = sum(nums)
    n = len(nums)
    intended_sum = n*(n+1) / 2
    return int(intended_sum - actual_sum)


nums = [0,3,1]
value = missingNumber(nums)
print(value)