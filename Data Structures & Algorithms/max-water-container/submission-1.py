class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        area=0
        while left<right:

            current_area=(right-left)*min(heights[left],heights[right])
            area=max(current_area,area)
            
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return area 
