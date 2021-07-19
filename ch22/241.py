# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import *

class Solution:
    depth = 0

    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.depth += 1
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    # print('[{}] {} {} {}'.format(self.depth, l, op, r))
                    results.append(eval(str(l) + op + str(r)))
            if self.depth == 1:
                print()
            return results
        
        if expression.isdigit():
            self.depth -= 1
            return [int(expression)]
        
        results = []
        for idx, op in enumerate(expression):
            if op in '-+*':
                # 연산자 기준으로 좌/우를 나눈다
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                results.extend(compute(left, right, op))
        self.depth -= 1

        return results

    def diffWaysToCompute2(self, expression: str) -> List[int]:
        if len(expression) < 2:
            return [int(expression)]
        ans = []
        m = {}
        op = {
            '*': lambda x, y: x * y,
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
        }

        def divideandconquer(s):
            if s in m:
                return m[s]
            left, right, res = [], [], []
            for i in range(len(s)):
                if s[i] in op:
                    s1 = s[0:i]
                    s2 = s[i + 1:]
                    left = divideandconquer(s1)
                    right = divideandconquer(s2)
                    for l in m[s1]:
                        for r in m[s2]:
                            res.append(op[s[i]](l,r))
            if not res:
                res.append(int(s))
            m[s] = res
            return res

        ans = divideandconquer(expression)
        return ans

s = Solution()
# print(s.diffWaysToCompute('2*3-4*5'))

# list
test = [1, 2, 3]
test.extend(test)
print('test1.extend(test1): {}'.format(test))
test = [1, 2, 3]
test.extend([4,5])
print('[1, 2, 3].extend([4,5]): {}'.format(test))
test = [1, 2, 3]
test.extend([[4,5],[6,7]])
print('[1, 2, 3].extend([[4,5],[6,7]]): {}'.format(test))
test = [1, 2, 3]
test.extend([[[4,5,6]]])
print('[1, 2, 3].extend([[[4,5,6]]])): {}'.format(test))

# tuple
test = [1, 2, 3]
test.extend((1, 2))
print('[1, 2, 3].extend((1, 2)): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5)))
print('[1, 2, 3].extend(((4, 5))): {}'.format(test))
test = [1, 2, 3]
test.extend((4, 5, 6))
print('[1, 2, 3].extend((4, 5, 6)): {}'.format(test))
test = [1, 2, 3]
test.extend(((4), (10)))
print('[1, 2, 3].extend(((4), (10))): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5), 10))
print('[1, 2, 3].extend(((4, 5), 10)): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5), (10)))
print('[1, 2, 3].extend(((4, 5), (10))): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5, 6), 10))
print('[1, 2, 3].extend(((4, 5, 6), 10)): {}'.format(test))
test = [1, 2, 3]
test.extend([(4, 5, 6), 10])
print('[1, 2, 3].extend([(4, 5, 6), 10]): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5, 6), (10)))
print('[1, 2, 3].extend(((4, 5, 6), (10))): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5), (10, 11)))
print('[1, 2, 3].extend(((4, 5), (10, 11))): {}'.format(test))
test = [1, 2, 3]
test.extend(((4, 5, 6), (10, 11, 12)))
print('[1, 2, 3].extend(((4, 5, 6), (10, 11, 12))): {}'.format(test))

# string
test = [1, 2, 3]
test.extend("456")
print('[1, 2, 3].extend("456"): {}'.format(test))
test = [1, 2, 3]
test.extend("abcde")
print('[1, 2, 3].extend("abcde"): {}'.format(test))
