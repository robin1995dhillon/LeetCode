#time O(N)
#Space O(N)
from collections import defaultdict


def containsDuplicate(nums):
    num_map = defaultdict(int)
    for num in nums:
        if(num_map[num]):
            return True
        num_map[num] += 1
    return False






nums = [1, 2, 3, 1]
print(containsDuplicate(nums))