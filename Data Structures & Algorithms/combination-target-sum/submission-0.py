class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #input: unique ints and target
        #output: unique combinations that add up to target
        #allowed to reuse int nums unlimited number of times
        #combination can contain 1 or more


        #like two sum??
        #decision tree where we have n decisions at each step
        #dfs backtrack to recursively traverse paths 
        #use target as a condition to stop extending the path

        #empty array to store results
        #sort nums in order

        #dfs func(index, current list, total):
            #if total == target
                #append copy of current list to res
                #return nothing
            
            #iterate through the list of nums starting at i
                #if total + num > target:
                    #return nothing
                #append num to current list
                #call dfs(j, current list, total + nums[j])
                #pop from current list
        
        #call dfs with 0, [], 0
        #return results

        res = []
        nums.sort()

        def dfs(i, curr, total):
            if total == target:
                #passing a reference bc want to save successful combinations
                res.append(curr.copy()) 
                return 
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop() #backtracking step for failed combinations
        dfs(0, [], 0)
        return res







