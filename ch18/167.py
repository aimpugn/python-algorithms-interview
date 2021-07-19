# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bi_search(num):
            numbers_len = len(numbers)
            result = None
            left = 0
            right = numbers_len - 1

            while left <= right and left < numbers_len and right < numbers_len:
                mid = left + (right - left) // 2
                if numbers[mid] > num:
                    right = mid - 1
                elif numbers[mid] < num:
                    left = mid + 1
                else:
                    result = mid
                    break

            return result
        ans = []
        idx = 0
        while idx < len(numbers):
            first = numbers[idx]
            result = bi_search(target - first)
            if result is not None and result != idx: # 같은 요소를 쓰지 말아야 한다
                return sorted([idx + 1, result + 1]) # 오름차순이어야 한다
            idx += 1
        
        return []

    def twoSum_two_pointers(self, numbers: List[int], target: int) -> List[int]:
        numbers_len = len(numbers)
        left = 0
        right = numbers_len - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        


s = Solution()

print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1, 0], -1))
print(s.twoSum([0, 0], -1))
print(s.twoSum_two_pointers([1,2,3,4,4,9,56,90], 8))
