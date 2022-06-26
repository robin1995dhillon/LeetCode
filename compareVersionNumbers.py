class Solution(object):
    def compareVersion(self, version1, version2):
        if version1 is None or version2 is None:
            return 0
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        difference = len(version2_list) - len(version1_list)
        if difference < 0:
            while len(version2_list) < len(version1_list):
                version2_list.append(0)
        elif difference > 0:
            while len(version1_list) < len(version2_list):
                version1_list.append(0)
        l = 0
        val = 0

        while l < len(version1_list):
            if int(version1_list[l]) > int(version2_list[l]):
                val = 1
                break
            elif int(version1_list[l]) < int(version2_list[l]):
                val = -1
                break
            elif int(version1_list[l]) == int(version2_list[l]):
                val = 0
            l = l + 1
        return val


s = Solution()
version1 = "0.1"
version2 = "1.1"
ans = s.compareVersion(version1, version2)
print(ans)
