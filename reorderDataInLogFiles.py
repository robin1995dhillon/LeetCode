class Solution(object):
    def reorderLogFiles(self, logs):
        dig_list = []
        letter_list = []
        l = 0
        for val in logs:
            if val.split(" ")[1].isdigit():
                dig_list.append(val)
            else:
                letter_list.append(val.split())
        letter_list.sort(key=lambda x: x[0])
        print(letter_list)
        letter_list.sort(key=lambda x: x[1:])
        print(letter_list)
        for i in range(len(letter_list)):
            letter_list[i] = " ".join(letter_list[i])

        letter_list.extend(dig_list)
        return letter_list


s = Solution()
# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
ans = s.reorderLogFiles(logs)

print(ans)
