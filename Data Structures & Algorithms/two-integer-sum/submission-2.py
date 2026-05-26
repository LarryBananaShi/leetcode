class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # key of desired value, index of what index it is in nums
        for i in range(len(nums)):
            desired = target - nums[i]
            if desired in seen:
                return[seen[desired],i]
            else:
                seen[nums[i]] = i