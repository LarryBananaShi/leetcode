class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #hashmap
        for i in range(len(nums)): 
            desired = target-nums[i] 
            if desired in seen:
                return [seen[desired], i]
            seen[nums[i]] = i