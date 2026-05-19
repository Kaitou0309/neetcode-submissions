class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_val = prices[0]
        sell_price = 0

        for i in prices: 
            
            if buy_val > i:
                buy_val = i
                
            diff = i - buy_val

            if diff > sell_price: 
                sell_price = diff

        return sell_price