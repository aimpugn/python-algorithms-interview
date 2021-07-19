import timeit
from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def decimal_to_binary(num, bit = 32):
            result = ""
            while num > 0:
                result = str(num % 2) + result
                num //= 2
            return result.rjust(bit, "0")

        ans = 0

        for num in nums:
            # print("=====================================================")
            # print("1. ans={}: {}".format(ans, decimal_to_binary(ans, 8)))
            # print("2. num={}: {}".format(num, decimal_to_binary(num, 8)))
            ans ^= num
            # print("3. ans={}: {}".format(ans, decimal_to_binary(ans, 8)))

        return ans

    def singleNumber2(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, times in counts.items():
            if times == 1:
                return num
    
s = Solution()
""" print(timeit.timeit(lambda: s.singleNumber([2,3,5,2,4,5,3,7,1,7,4,6,6]), number=100000))
print(timeit.timeit(lambda: s.singleNumber2([2,3,5,2,4,5,3,7,1,7,4,6,6]), number=100000))
print(timeit.timeit(lambda: s.singleNumber3([2,3,5,2,4,5,3,7,1,7,4,6,6]), number=100000)) """

print(s.singleNumber2([2,3,5,2,4,5,3,7,1,7,4,6,6]))