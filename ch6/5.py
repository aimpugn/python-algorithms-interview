# https://leetcode.com/problems/longest-palindromic-substring/
"""
Given a string s, return the longest palindromic substring in s.
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        s = "".join(s.split())
        print(s)
        s_len = len(s)
        longestPalindrome = s[0]
        longestPalindromeEnd = s_len - 1
        longestPalindromeMax = 0
        longestPalindromeStart = 0

        for i, c in enumerate(s):
            start = i
            start_old = start
            end = s_len - 1
            end_old = 0
            is_palindrome = False
            is_started = False
            loop_cnt = 0
            if end - start < longestPalindromeMax:
                break 
            
            while start < end:
                first = s[start]
                last = s[end]

                if first != last:
                    if is_started:
                        end = end_old
                        start = start_old
                        loop_cnt = 0
                        is_started = False
                        is_palindrome = False
                        longestPalindromeEnd = s_len - 1
                        longestPalindromeStart = 0
                    else:
                        end -= 1

                    continue
                else :
                    if loop_cnt == 0:
                        longestPalindromeStart = start
                        longestPalindromeEnd = end 
                        is_started = True
                        # 다음에 다시 시작할 end 지점
                        end_old = end - 1

                    if is_started: 
                        is_palindrome = True
                        loop_cnt += 1
                        start += 1
                        end -= 1

            if is_palindrome:
                if longestPalindromeMax < (longestPalindromeEnd - longestPalindromeStart):
                    longestPalindromeMax = longestPalindromeEnd - longestPalindromeStart
                    longestPalindrome = "".join(s[longestPalindromeStart:longestPalindromeEnd+1])

        return longestPalindrome

s = Solution()        
case = "babad"
# case = "cbbd"
case = "ac"
case = "acc"
case = "abbbddedssdeeaaas"
case = "xaabacxcabaaxcabaax"
# Time Limit Exceeded > 이제 시간을 줄이자
case = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(s.longestPalindrome(case))


