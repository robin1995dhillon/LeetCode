# Time - O(2*N) = O(N)
# we will loop over input to find summation, separate loop over set to find sum
# Space - O(N) => usage of set

def singleNumber(nums):
    unique_sum = sum(set(nums))
    intended_sum = sum(nums)
    return 2 * unique_sum - intended_sum


nums = [4, 1, 2, 1, 2]
value = singleNumber(nums)
print(value)
