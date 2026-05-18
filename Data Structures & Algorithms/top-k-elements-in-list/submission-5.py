class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the value is the count
        # the key is the number
        int_count = {}
        for num in nums:
            if num in int_count:
                int_count[num] +=1
            else:
                int_count[num] = 1

        sorted_ints = []
        for key, value in int_count.items(): #items turns into tuple [(x,y), (n,m)]
            sorted_ints.append([value,key]) # because sort work on the first in the list
        sorted_ints.sort(reverse = True)

        final = []
        for i in range(k):
            final.append(sorted_ints[i][1])

        return final




        