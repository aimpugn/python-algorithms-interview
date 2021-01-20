# 같은 레벨의 디렉토리 import https://stackoverflow.com/a/20076395
import sys
sys.path.insert(0, '.')
from pai_util.ch8.singly_linked_list import get_test_node

# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 노드 없거나 노드 하나라 다음 노드 없으면 True
        if head is None or head.next is None:
            return True

        # 리스트 노드의 끝은 어디일까? 모두 순회하기 전에는 알 수 없다
        # 그렇다면 순회하면서 대칭인지 확인을 해야 하는데...
        # 끝을 모르면서 대칭인지 확인할 수 있나? 없는 거 같다
        # 그럼 끝을 알 수 있게
        # 1. 자료 구조를 바꾸거나
        # 2. 다른 자료 구조의 도움을 받자
        compare: list = []        
        loop_cnt = 0
        while head:
            compare.append(head.val)
            head = head.next
            loop_cnt += 1

        left, right = 0, loop_cnt - 1
        while left < right:
            if compare[left] != compare[right]:
                return False
            left += 1
            right -= 1

        return True

s = Solution()
case = [1, 2, 3, 4]
case = [1, 2, 2, 1]

print(s.isPalindrome(get_test_node(case)))










