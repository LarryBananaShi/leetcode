class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap where the key is the integer, and the value is the number of times it shows up
        #once we populate the hashmap with a for loop, sort from smalles tto laargest value, then 
        # add the first k values to list, return that list
        integer_freq = {}
        for num in nums:
            if num in integer_freq:
                integer_freq[num] +=1;
            else:
                integer_freq[num] = 1
        
        sorted_items = sorted(integer_freq.items(), key=lambda x: x[1], reverse=True)
        final_list = []
        for i in range(k):
            final_list.append(sorted_items[i][0])
        return final_list




        

