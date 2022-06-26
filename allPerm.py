def allPerm(nums):
    result = []
    if (len(nums) == 1):
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = allPerm(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result


val_list = [1,2,3]
val = allPerm(val_list)
print(val)
