class Solution(object):
    def longestPalindrome(self, s):

        if len(s) == 0 or len(s) == 1 or self.palindrome(s):
            return s

        start = 0
        n = len(s)
        temp = n - 1
        ans = ""
        for i in range(n):
            end = n - 1
            value = i
            while (value <= end):
                if s[end] != s[value]:
                    end -= 1
                else:
                    str_val = s[value:end + 1]
                    if (self.palindrome(str_val)):
                        ans = max(ans, str_val, key=len)
                        break
                    else:
                        end -= 1
        return ans

        # txt = s[1:4]
        # print(txt)

    def palindrome(self, str_val):
        n = len(str_val)
        for i in range(0, int(len(str_val) / 2)):
            if (str_val[i] != str_val[n - i - 1]):
                return False
        return True

    def length(self, l1):
        print(max(l1))


s = "ahhhhhaahhhhha"
sol = Solution()
value = sol.longestPalindrome(s)
print(value)
# sol.length("zbc")
