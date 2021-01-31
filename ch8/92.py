import sys
sys.path.insert(0, '.')
from pai_util.ch8.singly_linked_list import get_test_node, ListNode, print_list_node

class Soltion:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == 0:
            return head
        
        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next

s = Soltion()
case = get_test_node([1, 2, 3, 4, 5, 6])
ans = s.reverseBetween(case, 2, 5)
