class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        area=0
        while left<right:

            area=max(area,(right-left)*min(heights[left],heights[right]))
            
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return area 
