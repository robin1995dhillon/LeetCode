class Solution(object):
    def generateParenthesis(self, n):
        output_list = []
        self.backtrack(output_list, "", 0, 0, n)
        return output_list

    def backtrack(self, output_list, current_string, open, close, max):
        if (len(current_string) == max * 2):
            output_list.append(current_string)
            return
        if (open < max):
            self.backtrack(output_list, current_string + "(", open + 1, close, max)
        if (close < open):
            self.backtrack(output_list, current_string + ")", open, close + 1, max)


sol = Solution()
value = sol.generateParenthesis(3)
print(value)
