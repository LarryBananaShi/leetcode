class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # put all values of word into hashmap
        # key is letter, value is number of times seen
        # compare 2 hash maps

        s_seen = {}
        t_seen = {}

        for c in s:
            if c in s_seen:
                s_seen[c] +=1;
                print("hi")
            else:
                s_seen[c] = 1;
        
        for c in t:
            if c in t_seen:
                t_seen[c] +=1;
            else:
                t_seen[c] = 1;

        if (s_seen == t_seen):
            return True
        else:
            return False
            
