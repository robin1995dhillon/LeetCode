class Solution(object):
    def divide(self, dividend, divisor):
        count = 0
        divid = abs(dividend)
        divis = abs(divisor)
        output = 0
        while divid >= divis:
            temp = divis
            mul = 1
            while divid >= temp:
                divid -= temp
                output += mul
                mul += mul
                temp += temp
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            output = -output

        return min(2147483647, max(-2147483648, output))


sol = Solution()
value = sol.divide(16, 3)
print(value)
