class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean = ""
        for c in s:
            if c.isalnum():
                s_clean+=c
        s_lower = s_clean.lower()
        left = 0
        right = len(s_lower)-1

        while (left<right):
            if s_lower[left] == s_lower[right]:
                left+=1
                right-=1
            else:
                return False
        
        return True


        