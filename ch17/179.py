import timeit
# https://leetcode.com/problems/largest-number/
from typing import *

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ''

        # 요소 단위로 크기 순으로 정렬
        # 맨 앞에서부터 자릿수 단위로 비교해서 크기 순으로 정렬
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                tmp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = tmp
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))

    def to_swap(self, n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber2(self, nums: List[int]) -> str:
        nums.sort(key = lambda x: x/(10**len(str(x))-1), reverse=True)
        return "0" if nums[0] == 0 else "".join(map(str,nums))

    def largestNumber3(self, nums: List[int]) -> str:
        def key_func(num):
            denominator = (10 **len(str(num))) - 1
            # denominator = 10 **(len(str(num)) - 1)
            key = num / denominator
            # print("largestNumber3: {} / {} to {}".format(num, denominator, key))
            return key
        nums = sorted(nums, key = key_func, reverse = True)
        # print(nums)
        return "0" if nums[0] == 0 else "".join(map(str,nums))

s = Solution()

# print(s.largestNumber3([10,2]))
# print(s.largestNumber3([3,30,34,5,9]))
# print(s.largestNumber3([3,3332,3453,3452,98,999,990]))
print(timeit.timeit(lambda: s.largestNumber([111311, 1113]), number=10000))
print(timeit.timeit(lambda: s.largestNumber2([111311, 1113]), number=10000))
print(timeit.timeit(lambda: s.largestNumber3([111311, 1113]), number=10000))