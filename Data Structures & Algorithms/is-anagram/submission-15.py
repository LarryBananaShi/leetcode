class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        letterCount_s = {}
        letterCount_t = {}

        if len(s_list) != len(t_list):
            return False

        for letter in s_list:
            if letter in letterCount_s:
                letterCount_s[letter] += 1
            else:
                letterCount_s[letter] = 1

        for letter in t_list:
            if letter in letterCount_t:
                letterCount_t[letter] += 1
            else:
                letterCount_t[letter] = 1

        return letterCount_s == letterCount_t
            



        # conditions:
        # must be equal length
        # if one character doesn't exist in the other, false
        # if equal lengths and same characters, but different amount of characters, false

    