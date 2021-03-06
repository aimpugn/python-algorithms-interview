# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

- 조건
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
from typing import *

class Solution:
    digits = ""
    result = []
    numbers = {
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': ['+'],
        '*': [],
        '#': []
    }

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.result = []
        if not self.digits:
            return self.result    

        self.dfs(0, "")

        return self.result

    # 재사용의 끝판왕
    def dfs(self, idx, letter_combination: str):
        # `dfs 함수를 멈출 때` 반환할 데이터와 자료 구조를 고려하려 기저 조건을 설정한다고 생각을 하자
        if len(letter_combination) == len(self.digits):
            self.result.append(letter_combination)
            return

        for i in range(idx, len(self.digits)):
            for j in self.numbers[self.digits[i]]:
                print("idx: ", idx, ", i: ", i, ", j: ", j, ", letter_combination + j: ", letter_combination + j)
                self.dfs(i + 1, letter_combination + j)


s = Solution()
digits = "2345"
print(s.letterCombinations(digits))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]


digits = ""
# []
