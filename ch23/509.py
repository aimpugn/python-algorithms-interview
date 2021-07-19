# https://leetcode.com/problems/fibonacci-number/
import timeit
import collections

class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        return self.fib_bottom_up(n)

    def fib_bottom_up(self, n):
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i -2]

        return self.dp[n]

    def fib_top_down(self, n):
        if n <= 1:
            return n
        
        if n in self.dp:
            return self.dp[n]
        
        self.dp[n] = self.fib_top_down(n - 1) + self.fib_top_down(n - 2)

        return self.dp[n]
    
    def fib_two_var(self, n):
        # x: 현재 피보나치 수
        # y: 다음 피보나치 수
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x
    
    def fib_matrix(self, n):
        import numpy as np
        M = np.matrix([[0, 1], [1, 1]])
        vec = np.array([[0], [1]])

        return np.matmul(M ** n, vec)[0]

        

s = Solution()

# print('fib_bottom_up:{}'.format(timeit.timeit(lambda: s.fib_bottom_up(30), number=10000)))
# print('fib_top_down:{}'.format(timeit.timeit(lambda: s.fib_top_down(30), number=10000)))
# print('fib_two_var:{}'.format(timeit.timeit(lambda: s.fib_two_var(30), number=10000)))
# print('fib_matrix:{}'.format(timeit.timeit(lambda: s.fib_matrix(30), number=10000)))

print('fib_bottom_up:{}, ({})'.format(s.fib_bottom_up(10000), timeit.timeit(lambda: s.fib_bottom_up(10000), number=1000)))
print('fib_top_down:{}, ({})'.format(s.fib_top_down(10000), timeit.timeit(lambda: s.fib_top_down(10000), number=1000)))
print('fib_two_var:{}, ({})'.format(s.fib_two_var(10000), timeit.timeit(lambda: s.fib_two_var(10000), number=1000)))
print('fib_matrix:{}, ({})'.format( s.fib_matrix(10000), timeit.timeit(lambda: s.fib_matrix(10000), number=1000)))
""" import cProfile
import pstats
pr = cProfile.Profile()
pr.enable()
for i in range(10000):
    # s.fib_bottom_up(30)
    # s.fib_top_down(30)
    s.fib_two_var(30)
    # s.fib_matrix(30)
pr.disable()
pstats.Stats(pr).print_stats() """
