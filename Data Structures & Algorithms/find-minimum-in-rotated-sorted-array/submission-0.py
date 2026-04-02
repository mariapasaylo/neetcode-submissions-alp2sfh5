class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Input: array of nums rotated
        #Output: min element of array

        #binary search
        #there are two parts that are sorted
        #unique elements so no duplicates
        
        #while left <= right:
            #left starts at 0
            #right starts at end 
            #if left > right
            #   search the right
            #else
            #   search the left
        
        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res =  min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return res 