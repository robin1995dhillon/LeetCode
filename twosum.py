#Time = O(N) loop array
# Space = O(N) create map
def twoSum(nums, target):
    num_map = {}
    length = len(nums)
    for i in range(0,length):
        goal = target - nums[i]
        if goal in num_map:
            return [num_map[goal],i]
        num_map[nums[i]] = i










nums = [2, 7, 11, 15]
target = 9

twoSum(nums,target)
# print(value)