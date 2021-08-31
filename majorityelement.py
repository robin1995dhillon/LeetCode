# Time O(2*N) = O(N)
# Space O(N)

def majorityElement(nums):
    num_map = {}
    for i in nums:
        num_map[i] = num_map.get(i, 0) + 1
    for num in nums:
        if (num_map[num] > len(nums) // 2):
            return num


nums = [2, 2, 1, 1, 1, 2, 2]
value = majorityElement(nums)
print(value)
