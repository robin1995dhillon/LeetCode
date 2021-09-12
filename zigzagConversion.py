class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mp = {}
        if numRows == 1:
            return s
        for i in range(numRows):
            mp[i] = []
        row = 0
        down = 0
        for c in s:
            print(row)
            mp[row].append(c)
            if row == 0:
                down = 1
            elif row == numRows-1:
                down = -1
            row = row + down
        print(mp)
        res = ""
        for i in mp.keys():
            res += "".join(mp[i])
        return res





s = "PAYPALISHIRING"
numRows = 4
sol = Solution()
value = sol.convert(s,numRows)
print(value)
