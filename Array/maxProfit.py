# Say you have an array prices for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time 
# (i.e., you must sell the stock before you buy again).
# e.g [7,1,5,3,6,4]
# answer = 7
class Solution(object):
    def maxProfit(self, prices):
        i = 0
        low = prices[0]
        high = prices[0]
        score = 0
        while i < len(prices)-1:
            # check what is the smallest number in this iteration
            #inner loop is buy
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i+=1
            low = prices[i]

            #check what is the continuously largernumber
            # sell when next number is less.
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i+=1
            high = prices[i]
            score += high - low

        return score


def main():
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))

    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))



if __name__ == "__main__":
    main()