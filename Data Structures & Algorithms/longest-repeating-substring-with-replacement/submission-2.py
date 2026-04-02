class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #input: 
        #   string of capital letters
        #   integer k
        #output:
        #   length of longest substring with only one character

        # k num of characters we can change in s
        #find the longest using two pointers
        #replace the letters that don't match current longest
        #return length of longest substring

        #left at 0
        #store count = most frequent using dictionary
        #store maxFreq = 0
        #res = 0
        #iterate through s using right pointer
        #   increment count freq s[r]
        #   update maxFreq
        #   while length of current substring - maxFreq > k
        #       decrement counter s[left]
        #       increment left pointer
        #
        #   update res with max res
        #return res
        
        l = 0
        count = {}
        maxFreq = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq,count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
            


