class Solution:

    def encode(self, strs: List[str]) -> str:
        #convert list to string
        #use non ascii character as delimiter
        #for every string write length + string

        res = ""
        for s in strs:
            str_len = len(s)
            res +=  str(str_len) + "+" + s
        return res 

    def decode(self, s: str) -> List[str]:
        #convert string to list using delimiter
        #use apointer to keep track of current index
        #while we are i nbound of the current word in the string 
        #   move pointer until we find +
        #   extract the length and that is exactly the length of the string to be stored in a list
        #   move i forward by the length
        #retrun strings

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "+":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res

