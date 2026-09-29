class Solution:

    def encode(self, strs: List[str]) -> str:
        # for every string in strs, add a # and the number of chars in that string
        encoded = ''
        for string in strs:
            encoded += (str(len(string)) + '#'+ string)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        string =''
        while (i < len(s)):
            j = i
            while (s[j] != '#'): #get the # of chars in the upcoming word
                j+=1
            print("the number is ", s[j])
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            
            i = 1 + j + length
        return decoded
