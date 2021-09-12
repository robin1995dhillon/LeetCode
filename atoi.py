import re
class Solution(object):
    def myAtoi(self, s):
        value = s.strip()
        vals = ''
        m = re.match(r'\s*([\+\-]?\d+)', s)
        if m is None:
            return 0
        else:
            val = m.group(1)
        max = (2 ** 31) - 1
        min = -(2 ** 31)
        if val[0] == "+":
            val = val[1:]
        # for i in range(len(val)):
        #     if ((value[i] == "-" or value[i] == "+") and i == 0):
        #         val = value[i]
        #     elif value[i].isnumeric() == False:
        #         break
        #     else:
        #         val += value[i]
        # if val is None or val == "":
        #     return 0
        if int(val) > max:
            val = max
        elif int(val) < min:
            val = min
        return int(val)


sol = Solution()
s = "00000-42a1234"
answer = sol.myAtoi(s)
print(answer)
