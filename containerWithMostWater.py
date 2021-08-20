def maxArea(height):
        left = 0
        right = len(height) - 1
        maxarea = 0
        while (left <= right):
            maxarea = max(maxarea, (min(height[left], height[right]) * (right - left)))

            if(height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1

        print(maxarea)


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
maxArea(height)
