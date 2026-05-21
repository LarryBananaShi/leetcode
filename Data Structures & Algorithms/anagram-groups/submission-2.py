class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {} #track letter count (key) to values (strs) #
        #edit: can use count = defaultdict(list) to automatically assign missing values, if block can be removed
        for word in strs:
            array = [0]*26 # array of 26 0s

            for char in word:
                array[ord(char)- ord("a")] +=1
            
            if tuple(array) in count:
                count[tuple(array)].append(word)
            else:
                count[tuple(array)] = [word]



        return list(count.values())