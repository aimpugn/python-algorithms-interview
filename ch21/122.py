# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    def maxProfit_3rd(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]: # 트랜잭션은 이뤄진다고 치고, 올라가는 값만 계산
                result += prices[i + 1] - prices[i]
        return result

    def maxProfit_2nd(self, prices: List[int]) -> int:
        '''
        - `구매`: 전날보다 가격이 내려간 경우
        - `유지`: 다음날 가격이 올라간 경우
        - `판매`: 다음날 가격이 내려감
        '''
        prices_len = len(prices)
        if prices_len == 0:
            return 0

        idx = 0
        profit = 0
        current = 0
        is_bought = False
        while idx < prices_len:
            if (idx + 1 < prices_len and prices[idx] > prices[idx + 1]) or idx == prices_len - 1: # 다음날 가격이 내려감 또는 끝에 도달
                if is_bought: # 구매한 주식이 있으면 판매
                    profit += prices[idx] - current
                    is_bought = False
                # 없으면 스킵
            elif not is_bought and prices[idx] < prices[idx + 1]: # 전날보다 가격이 내려가고, 다음날 가격이 올라감
                is_bought = True
                current = prices[idx]
            idx += 1
        
        return profit

    def maxProfit_1st(self, prices: List[int]) -> int:
        '''
        - `구매`: 전날보다 가격이 내려간 경우
        - `유지`: 다음날 가격이 올라간 경우
        - `판매`: 다음날 가격이 내려감
        '''
        prices_len = len(prices)
        if prices_len == 0:
            return 0
        idx_max = prices_len - 1
        idx = 0
        profit = 0
        current = 0
        is_bought = False
        while idx < prices_len:
            if (idx + 1 <= idx_max and prices[idx] > prices[idx + 1]) or idx == idx_max: # 다음날 가격이 내려감
                if is_bought:
                    profit += prices[idx] - current
                    is_bought = False
            elif idx > 0 and prices[idx - 1] > prices[idx] and prices[idx] < prices[idx + 1]: # 전날보다 가격이 내려가고, 다음날 가격이 올라감
                if not is_bought:
                    is_bought = True
                    current = prices[idx]
            elif prices[idx] < prices[idx + 1]: # 다음날 가격이 올라감
                if not is_bought:
                    is_bought = True
                    current = prices[idx]

            idx += 1
        
        return profit
    
s = Solution()

print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([5, 4, 3, 2, 1]))
print(s.maxProfit([5, 1, 4, 3, 2]))
print(s.maxProfit([5]))


for i in range(7):
    print(i, end = " ")