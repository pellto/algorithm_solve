class Solution:
    def maxProfit(self, prices):
        buy_price, profit = prices[0], 0
        for i in range(1, len(prices)):
            print(f"MEMO : {[buy_price, profit]}\n")
            if prices[i] < buy_price:
                buy_price = prices[i]
            if profit < prices[i] - buy_price:
                profit = prices[i] - buy_price
        return profit


if __name__=="__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
