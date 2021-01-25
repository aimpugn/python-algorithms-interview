"""
코드 참조 링크:
https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/#singlelinkedlist
https://github.com/clair3st/Data-Structures/blob/master/src/linked_list.py
"""
class SinglyLinkedList(object):
    class Node(object):
        def __init__(self, data, next: 'Node' = None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self._length = 0
        self.node_start = None
    
    """
    처음에 삽입
    """
    def insert_at_start(self, data) -> bool:
        # 새로운 노드 생성
        node_new = self.Node(data, self.node_start)
        # 시작 노드에 새로 생성한 노드로 할당
        self.node_start= node_new
        self._length += 1

        return True
    
    """
    끝에 삽입
    """
    def insert_at_end(self, data) -> bool:
        node_new = self.Node(data)
        # 시작도 없다면 시작 지점에 삽입
        if self.node_start is None:
            self.node_start = node_new
            self._length += 1
            return True

        node_curr = self.node_start
        while node_curr.next is not None:
            node_curr = node_curr.next

        node_curr.next = node_new
        self._length += 1
        return True

    """
    특정 요소 다음에 삽입
    """
    def insert_after_item(self, target, data) -> bool:
        node_curr = self.node_start
        # 대상 값을 가진 노드가 있는지 확인
        while node_curr is not None:
            if node_curr.data == target:
                break
            node_curr = node_curr.next
        # 없으면 False
        if node_curr is None:
            return False

        # 새로운 노드 생성
        node_new = self.Node(data, node_curr.next)
        # target 가진 노드 다음 노드를 새로 생성한 노드로 할당
        node_curr.next = node_new
        self._length += 1
        return True

    """
    특정 요소 전에 삽입
    """
    def insert_before_item(self, target, data) -> bool:
        node_curr = self.node_start
        if node_curr is not None and node_curr.data == target:
            node_new = self.Node(data, node_curr)
            self.node_start = node_new
            self._length += 1
            return True

        after = None
        before = None
        # 전 요소와 다음 요소 사이에 넣어야 하므로, `전 요소` 탐색 필요
        while node_curr and node_curr.next is not None:
            if node_curr.next.data == target:
                after = node_curr.next
                before = node_curr
                break
            node_curr = node_curr.next

        # 없으면 False
        if after is None or before is None:
            return False

        # 새로운 노드 생성
        node_new = self.Node(data, after)
        # 전 노드 다음, 이 노드 전
        before.next = node_new
        self._length += 1
        return True

    """
    특정 인덱스에 삽입
    node_start의 인덱스는 0
    """
    def insert_at_index(self, index, data) -> bool:
        if index < 0:
            return False

        if index == 0:
            return self.insert_at_start(data)

        node_curr = self.node_start
        if node_curr is None:
            return False

        # index 위치에 들어가야 하므로, index 전 위치의 노드를 구해야 한다
        index_next = 1 # 인덱스 매개변수와 비교할 `노드의 다음 인덱스`
        node_index_before = None
        while node_curr is not None:
            if index_next == index:
                node_index_before = node_curr
            index_next += 1
            node_curr = node_curr.next

        if node_index_before is None:
            return False
        else:
            node_new = self.Node(data, node_index_before.next)
            node_index_before.next = node_new
            self._length += 1
            return True

    def get_start_node(self) -> Node:
        return self.node_start

    def get_length(self) -> int:
        return self._length
    """
    노드 출력
    """
    def print_singley_linked_list(self):
        print('[', end = '')
        loop_max = self.get_length()
        loop_cnt = 0
        node_curr = self.node_start
        while node_curr is not None and loop_cnt < loop_max:
            print(str(node_curr.data), end = '')
            if node_curr.next is not None:
                print(' -> ', end = '')
            node_curr = node_curr.next
            loop_cnt += 1
        print(']')
    
    """
    리트코드 노드 페어 스왑 문제
    """
    def swap_node_pair(self) -> bool:
        loop_max = self.get_length()
        loop_cnt = 0
        node_curr = self.node_start # 유효한 노드인지 검증할 `현재 노드` 초기화
        while node_curr is not None and loop_cnt < loop_max:
            tmp = node_curr
            # 다다음 노드 준비
            node_nnext = None
            if node_curr.next.next:
                node_nnext = node_curr.next.next
            
            # 현재 노드에 다음 노드 
            node_curr = node_curr.next
            self.print_singley_linked_list()
            # 다음 노드에 과거 현재 노드
            node_curr.next = tmp # 이 코드가 문제. 왜? 111 -> 2 -> 111 -> 2... 무한 반복
            self.print_singley_linked_list()
            node_curr.next.next = node_nnext
            self.print_singley_linked_list()
            node_curr = node_curr.next.next
            loop_cnt += 1

            
