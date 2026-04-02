class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input is an array integers heights
        #choose two bars to form a container and return max amount of water

        #2 pointers
        #want to maximize width and height
        #area = min(height[i], height[j]) * (j-i)

        #left at 0
        #right at end or array
        #res = 0

        #while left < right
        #   area = min(height[i], height[j]) * (j-i)
        #   res = max(res, area) 
        #   if left < right
        #       increment left
        #   else
        #       decrement right
        # return res

        left, right = 0, len(heights) - 1
        res = 0
        area = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res

       