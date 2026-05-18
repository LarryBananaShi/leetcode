class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key is the number
        # value is the length of the consecutive sequence it's a part of

        hashmap = {}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                if (nums[i]+1) in hashmap:
                    hashmap[nums[i]]+=hashmap[nums[i] + 1]
                if (nums[i]-1) in hashmap:
                    hashmap[nums[i]]+=hashmap[nums[i] - 1]
        if not hashmap:
            maxval = 0
        else:
            maxval = max(hashmap.values())
        return maxval
             
            
