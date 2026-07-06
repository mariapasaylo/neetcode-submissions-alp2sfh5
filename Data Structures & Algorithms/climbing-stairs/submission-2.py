class Solution:
    def climbStairs(self, n: int) -> int:
        #input integer n
        #output distinct ways to sum up to given integer

        #similar to knapsack problem?
        #DP and memoization to store sums top-down
        #odd and even case
        #options to add 1 or 2
        #recursion
        #start with i = 0
        #base case if i==n then return 0

        #store results
        cache = [-1] * n

        def step(i):
            #invalid path
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = step(i+1) + step(i+2)
            return cache[i]
        return step(0)
            
            

        



        