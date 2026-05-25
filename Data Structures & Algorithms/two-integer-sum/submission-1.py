class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key is value, value is index 
        seen = {}
        for i in range(len(nums)):
            desired = target - nums[i]
            if desired in seen:
                return [seen[desired],i]
            else:
                seen[nums[i]] = i
