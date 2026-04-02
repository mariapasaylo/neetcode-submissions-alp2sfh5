class Solution:
    def isPalindrome(self, s: str) -> bool:
        #string input with alphanumeric char
        #true of palindrome. Otherwise, false

        #two pointers start at 0 and end

        #remove nonalphanumeric characters and change to lowercase
        #while left < right
        #   if left != right:
        #       return False
        #   increment left
        #   decrement right
        #return True

        s_clean = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        left = 0
        right = len(s_clean) - 1

        while left < right:
            if s_clean[left] != s_clean[right]:
                return False
            left += 1
            right -= 1
        
        return True