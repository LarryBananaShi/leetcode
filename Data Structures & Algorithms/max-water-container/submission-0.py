class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height: smaller of the two indexes
        # width: index distance between the indexes
        # output: height * width
        right = len(heights)-1
        left = 0
        current_max = 0

        while(left != right):
            amount = (right-left) * min(heights[right], heights[left])
            print(amount)
            if (amount > current_max):
                current_max = amount;
            if (heights[right] > heights[left]):
                left+=1
            elif (heights[right] < heights[left]):
                right-=1
            elif (heights[right] == heights[left]):
                right-=1

        return current_max
            
