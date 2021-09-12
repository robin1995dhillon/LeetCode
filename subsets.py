class Solution(object):
    def subsets(self, nums):
        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)
        return ans

    def solution(self, nums, ans, cur, index):
        if (index >= len(nums)):
            return
        ans.append(cur[:])
        for i in range(index,len(nums)):
            if(nums[i] not in cur):
                cur.append(nums[i])
                self.solution(nums,ans,cur,i)
                cur.pop()
        return
