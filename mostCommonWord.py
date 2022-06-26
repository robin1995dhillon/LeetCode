import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        s = re.sub("[^a-zA-Z0-9]", " ", paragraph).lower()
        new_list = s.split()
        print(s)
        print(new_list)
        map_para = {}
        ans = -1
        final_val = ""
        for val in new_list:
            if val not in banned:
                if val not in map_para:
                    map_para[val] = 0
                else:
                    map_para[val] += 1
                if map_para[val] > ans:
                    ans = map_para[val]
                    final_val = val
        print(map_para)
        return final_val



s = Solution()
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
paragraph = "a.a.a.a.a.a.a"
banned = []
# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]
answer = s.mostCommonWord(paragraph, banned)
print(answer)