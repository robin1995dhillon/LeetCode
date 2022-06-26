def fourSumCount(nums1, nums2, nums3, nums4):
    map_val = {}
    ans = 0
    for i in nums1:
        for j in nums2:
            if (i + j not in map_val):
                map_val[i + j] = 0
            map_val[i + j] += 1
    for i in nums3:
        for j in nums4:
            target = -(i + j)
            if (target in map_val):
                ans += map_val[target]
    return ans


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
value = fourSumCount(nums1, nums2, nums3, nums4)
print(value)