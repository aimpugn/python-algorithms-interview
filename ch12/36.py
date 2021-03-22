# https://leetcode.com/problems/combination-sum/

from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(candidates, combination, sum_curr):
            if sum_curr > target:
                return
            if sum_curr is target:
                ans.append(combination)


        return ans