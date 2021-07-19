import time
import timeit
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def decimal_to_binary(num, bit = 8):
            result = ""
            while num > 0:
                result = str(num % 2) + result
                num //= 2
            return result.rjust(bit, "0") if bit > 0 else result


        return decimal_to_binary(x ^ y, 0).count("1")

    def hammingDistance2(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
    def hammingDistance3(self, x: int, y: int) -> int:
        m = max(x, y)
        n = min(x, y)

        bits = 0

        while m:
            r1 = m % 2 == 0 
            r2 = n % 2 == 0
            
            if r1 != r2:
                bits += 1
                
            m >>= 1
            n >>= 1
            
        return bits

    def hammingDistance4(self, x: int, y: int) -> int:
        res = x^y
        count = 0
        
        for i in range(32):
            if res&1:
                count+=1
            res = res>>1
            
        return count        


s = Solution()

""" print(s.hammingDistance(1, 4))
print(s.hammingDistance(3, 1))
print(s.hammingDistance(0, 0)) 
print(s.hammingDistance(30, 2147483647))"""

print(timeit.timeit(lambda: s.hammingDistance(43243, 2147483647), number=10000))
print(timeit.timeit(lambda: s.hammingDistance2(43243, 2147483647), number=10000))
print(timeit.timeit(lambda: s.hammingDistance3(43243, 2147483647), number=10000))
print(timeit.timeit(lambda: s.hammingDistance4(43243, 2147483647), number=10000))

# cnt_try = 100000
# start = time.time()
# for i in range(cnt_try): s.hammingDistance(43243, 2147483647)
# end = time.time()
# print('hammingDistance: {}'.format(end - start))

# start = time.time()
# for i in range(cnt_try): s.hammingDistance2(43243, 2147483647)
# end = time.time()
# print('hammingDistance2: {}'.format(end - start))

# start = time.time()
# for i in range(cnt_try): s.hammingDistance3(43243, 2147483647)
# end = time.time()
# print('hammingDistance3: {}'.format(end - start))
