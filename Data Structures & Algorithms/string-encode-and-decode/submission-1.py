class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded=""
        for string in strs:
            encoded += str(len(string)) + "#" +string # ex. 4#test
                
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        current_string=""
        decoded=[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j]) #get the number value to the left of # to determine length
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length

        return decoded

