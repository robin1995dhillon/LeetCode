class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if haystack is None or needle is None:
            return -1
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1




s = Solution()
val = "bba"
haystack = ""
ans = s.strStr(haystack,val)
print(ans)