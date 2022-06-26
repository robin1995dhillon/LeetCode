def searchRange(nums, target):
    left = getLeft(nums,target)
    right = getRight(nums,target)
    return [left,right]


def getLeft(nums, target):
    start = 0
    end = len(nums) - 1

    while (start <= end):
        mid = (start + end) // 2
        if (nums[mid] == target):
            if (mid == 0 or nums[mid - 1] != target):
                return mid
            end = mid - 1
        elif (nums[mid] > target):
                end = mid - 1
        else:
                start = mid + 1
    return -1


def getRight(nums, target):
    start = 0
    end = len(nums) - 1

    while (start <= end):
        mid = (start + end) // 2
        if (nums[mid] == target):
            if (mid == end or nums[mid + 1] != target):
                return mid
            start = mid + 1
        elif (nums[mid] < target):
                start = mid + 1
        else:
                end = mid - 1
    return -1

nums = [1,2,3]
target = 1
a = searchRange(nums, target)
print(a)