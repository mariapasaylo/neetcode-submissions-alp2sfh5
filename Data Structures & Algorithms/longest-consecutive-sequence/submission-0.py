class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input unordered array of integers
        #output length of res (i.e. list of consecutive numbers)

        #finding if consecutive numbers exist in unsorted array
        #sort them and check if next number is 1 more than before
        #notice that each number does not have to be start of a sequence curr_num -1 dne
        # use a hash set

        #store result
        #store integers in a hashset
        #for each num in nums
        #   while num-1 in hashset (means that start of sequence)
        #       append num-1 to result
        #return size of result

        num_set = set(nums)
        length = 0
        longest = 0
        for num in num_set:
            if num - 1 not in num_set: # check if n is the start of the sequence
                length = 1
                while num + length in num_set: # build sequence
                    length += 1
                longest = max(length,longest)
        
        return longest


        