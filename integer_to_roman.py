class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        res = ''
        i = 10
        while num > 0:
            mod = num % 10
            num //= 10
            if mod == 9:
                res = roman[i / 10] + roman[i] + res
            elif mod == 4:
                res = roman[i / 10] + roman[i / 2] + res
            elif mod < 5:
                res = roman[i / 10] * mod + res
            elif mod >= 5:
                res = roman[i / 2] + roman[i / 10] * (mod - 5) + res
            i *= 10
        return res


num = 984
s = Solution()
val = s.intToRoman(num)
print(val)
