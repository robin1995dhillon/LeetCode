class Solution(object):
    def trap(self, height):
        l = 0
        r = 0
        area = 0
        while l < len(height) - 1:
            l += 1
            r = l + 1
            if height[l] > 0:
                while height[r] < height[l]:
                    r += 1
                area += (height[r] - height[l]) * (r - l)
                l = r - 1
        return area


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]sdfsdfsd
ans = s.trap(height)
print(ans)
