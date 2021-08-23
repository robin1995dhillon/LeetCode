# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(mid):
    first_bad_version = 3
    return mid >= first_bad_version


class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while (left < right):
            mid = (left + right) // 2
            if (not isBadVersion(mid)):
                left = mid + 1

            else:
                right = mid

        return left

s = Solution()
answer = s.firstBadVersion(10)
print(answer)