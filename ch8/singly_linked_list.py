class SingleyLinkedList(object):
    class Node(object):
        def __init__(self, data, next: 'Node' = None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.start = None
    
    """
    처음에 삽입
    """
    def insert_at_start(self, data):
        # 새로운 노드 생성
        new = self.Node(data, self.start)
        # 시작 노드에 새로 생성한 노드로 할당
        self.start= new
    
    """
    끝에 삽입
    """
    def insert_at_end(self, data):
        new = self.Node(data)
        # 시작도 없다면 시작 지점에 삽입
        if self.start is None:
            self.start = new
            return
        curr = self.start
        while curr.next is not None:
            curr = curr.next
        curr.next = new

    """
    특정 요소 다음에 삽입
    """
    def insert_after_item(self, target, data) -> bool:
        curr = self.start
        # 대상 값을 가진 노드가 있는지 확인
        while curr is not None:
            if curr.val == target:
                break
            curr = curr.next
        # 없으면 False
        if curr is None:
            return False
        else:
            # 새로운 노드 생성
            new = self.Node(data, curr.next)
            # target 가진 노드 다음 노드를 새로 생성한 노드로 할당
            curr.next = new

    def print_singley_linked_list(self):
        print('[', end = '')
        curr = self.start
        while curr is not None:
            print(str(curr.data), end = '')
            if curr.next is not None:
                print(' -> ', end = '')
            curr = curr.next
        print(']')