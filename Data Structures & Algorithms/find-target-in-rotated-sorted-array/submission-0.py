class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: rotated array and target
        #output: index of target

        #binary search because sorted and it is just shifted
        #find where the rotation is located aka deflection point

        #left = 0
        #right = end of array
        #while left <= right
        #   mid = (left + right) // 2
        #   base case if target == mid
        #       return mid
        #   
        #   if nums[left] <= nums[mid]
        #       if target > mid or target < left -> means that target is in the right half
        #           increment left mid + 1
        #       else -> means target is in the left
        #           decrement right mid - 1
        #   else
        #       if target < mid or target > right -> means target is in the left half
        #           decrement right mid - 1
        #       else
        #           increment left mid + 1
        # return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

