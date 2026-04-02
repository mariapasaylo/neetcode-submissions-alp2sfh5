class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input array with prices int and i represents the day
        #choose day and buy and future day to sell
        #output max profit

        #want lowest and buy day and highest sell day
        #two pointers
        #left must be lower than right

        #left start 0
        #right start at 1
        #maxProfit = 0
        #while r < len(prices)
        #   if price[l] < price[r]
        #       compute max profit
        #   else:
        #       increment left 
        #   increment right
        #return maxProfit
        l, r = 0,1
        res = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res