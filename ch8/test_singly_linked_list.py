import sys
sys.path.insert(0, '.')
from singly_linked_list import SinglyLinkedList


sll = SinglyLinkedList()
sll.insert_at_index(0, 9999)
sll.insert_at_start(1)
sll.insert_before_item(1, 111)
sll.insert_at_start(2)
sll.insert_at_index(2, 5)
sll.insert_at_index(5, 5)
sll.print_singley_linked_list()
sll.swap_node_pair()
    




