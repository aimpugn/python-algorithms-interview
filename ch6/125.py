import re
# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        sLen = len(s)
        if sLen == 0:
            return True
        
        a: bool = False
        s = s.lower()
        start = 0
        end = sLen - 1
        loopCnt: int = 0 
        while start <= end :
            if not s[start].isalnum():
                start += 1
                continue
            elif not s[end].isalnum():
                end -= 1
                continue
            else :
                if s[start] == s[end]:
                    a = True
                    loopCnt += 1
                    start += 1
                    end -= 1
                else :
                    loopCnt += 1
                    a = False
                    break
        
        if loopCnt == 0: 
            a = True

        return a

    '''
    Runtime: 32 ms, faster than 98.15% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 15.7 MB, less than 21.26% of Python3 online submissions for Valid Palindrome.
    '''
    def second(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s).lower()
        mid = len(s) // 2

        return s[:mid] == s[:-mid - 1:-1] # 역순일 경우 -1부터 시작하므로, -mid에 1을 더 빼준다

s= Solution()
case: str = "1b1"
a = s.isPalindrome(s = case)
print(a)
print(s.second("A man, a plan, a canal: Panama"))
print(s.second("0P"))