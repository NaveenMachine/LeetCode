"""
    Strategy is to find the area of water. (r - l) x minimum (heights[r], heights[l]) is the distance
    between the 2 bars. 
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        areas = []

        r = len(heights) - 1

        for i, a in enumerate(heights):
            if i == len(heights) - 1:
                break
            r = len(heights) - 1
            while i < r:
                length = r - i

                height = min(a, heights[r])

                areas.append(length * height)

                r -= 1

        areas.sort()

        if areas:
            return areas[-1]
        else:
            return 0
            
        
    def betterMaxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:

            area = min(heights[l], heights[r]) * (r - 1)

            res = min(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        
        return res





        