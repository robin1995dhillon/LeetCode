class Solution(object):
    def firstUniqChar(self, s):
        map_val = {}
        for i in range(len(s)):
            if s[i] not in map_val:
                map_val[s[i]] = [i,0]
            else:
                map_val[s[i]][1] += 1
        # print(map_val)
        for key, value in map_val.items():
            if value[1] == 0:
                return value[0]
            else:
                continue
        return -1


sol = Solution()
val = "aabvdd"
ans = sol.firstUniqChar(val)
print(ans)
