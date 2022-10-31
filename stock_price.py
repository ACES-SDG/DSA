from typing import List


class Solution:
    def maxProfit(self, prices :List[int]) -> float:
        # print(prices)
        # print(min(prices))
        # print(len(prices)-1)

        if  min(prices) == prices[len(prices)-1]:
            return 0
        for i in range(len(prices)):
            min_ = min(prices)
            max_ = max(prices)
            # print(prices.index(max_) )
            if prices.index(max_) == 0:
                prices.pop(0)
                # print(prices)
            if max_ in prices:
                if prices.index(max_) > prices.index(min_):
                    profit = max_-min_

                    print(profit)
                    return profit

obj = Solution()
res = obj.maxProfit(prices=[2,4,1])

print(res,'res')
