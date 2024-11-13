class singleLinkedList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, data):
        self.head = self.Node(data, self.head)
        self.size += 1

    def insert_after(self, data, p):    # 노드 p 뒤에 새로는 노드 추가
        if p is not None:
            p.next = self.Node(data, p.next)
            self.size += 1
    
    def delete_front(self):
        if self.is_empty():
            raise
        self.head = self.head.next

class EmptyError(Exception):
    pass