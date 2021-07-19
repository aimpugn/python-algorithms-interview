# https://leetcode.com/problems/sort-colors/
from typing import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red = 0
        # white = 1
        # blue = 2
        # 인접하는 제자리 정렬
        # - 제자리 정렬? 추가적인 메모리 공간이 많이 필요하지 않거나 필요 없는 알고리즘.
        # - 추가적인 메모리 공간 할당하지 않는 경우
        # 2분할 하는 퀵정렬 개선. 특히 중복되는 입력값이 많을 때 퀵정렬 퍼포먼스가 좋지 않음
        # 0, 1, 2에 대한 3분할과 정렬 필요. 같은 값은 중간으로 모으고, 작은 값은 좌로, 큰 값은 우로,
        # 작은 값 마지막 인덱스 반환. 큰 값 첫 인덱스 반환 
        
        self.quick_sort(nums, 0, len(nums) - 1)
    

    def quick_sort(self, nums, start, end):
        if start >= end:
            return

        def partition(nums, start, end):
            pivot = nums[(end - start) // 2]
            print("nums:{}, start:{}, end:{}, pivot:{}".format(nums, start, end, pivot))

            while start < end:
                if nums[start] < pivot:
                    start += 1
                    print("nums[start]:{}, start:{}".format(nums[start], start))
                elif nums[end] > pivot:
                    end -= 1
                    print("nums[end]:{}, end:{}".format(nums[end], end))
                else:
                    break

            nums[start], nums[end] = nums[end], nums[start]
            print("nums:{}".format(nums))

            return start, end
        
        i, j = partition(nums, start, end)
        mid = (j - i) // 2 
        
        self.quick_sort(nums, i, mid)
        self.quick_sort(nums, mid, len(nums) - 1)

        

s = Solution()

s.sortColors([2, 0, 2, 1, 1, 0])
