class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {} #track letter count (key) to values (strs)
        for word in strs:
            array = [0]*26 # array of 26 0s

            for char in word:
                array[ord(char)- ord("a")] +=1
            
            if tuple(array) in count:
                count[tuple(array)].append(word)
            else:
                count[tuple(array)] = [word]



        return list(count.values())
            
            
            #for each string, make an array that has all 26 letters and holds count for each letter
            #if array in hashmap (use array as key), store value of current str into array at that key value



        #first solution
        #for every single string in the string list, we need to
        #hashmap with a key value pair where the key is a letter and the 
        #value is the frequency of that letter. add each of these hash maps
        #to a new list

        #this is one for loop ^

        #now that we have all the hash maps in the list, we iterate through that list
        #and group similar pairs