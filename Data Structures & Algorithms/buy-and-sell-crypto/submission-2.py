class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input array with prices int and i represents the day
        #choose day and buy and future day to sell
        #output max profit

        #dp
        #maximizing profit = sell - buy
        
        #maxProfit  = 0 
        #minBuy being first price in list
        #iterate through prices as sell days
        #   maxProfit = max(maxProfit, sell - minBuy)
        #   minBuy = min(minBuy,sell)
        #return maxProfit

        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return maxProfit