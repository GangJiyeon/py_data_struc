'''
__init__: 리스트 초기화
get_size: 리스트 노드 개수 반환
is_empty: 리스트가 비었는지 확인
insert_front: 리스트 맨 앞에 노드 삽입
insert_after: 특정 노드 뒤에 노드 삽입
delete_front: 첫 번째 노드 삭제
delete_after: 특정 노드 뒤의 노드 삭제
search: 특정 값을 가진 노드의 위치 반환
print_list: 리스트의 모든 노드 출력
EmptyError: 비어있는 리스트 조작 시 발생하는 예외
'''

class Slist:  # 단순 연결 리스트(Singly Linked List) 클래스 정의
    class Node:  # 리스트의 각 노드를 나타내는 내부 클래스 정의
        def __init__(self, item, link):  # 노드 생성자
            self.item = item  # 노드의 데이터 필드, 저장할 값
            self.next = link  # 노드의 링크 필드, 다음 노드를 가리킴

    def __init__(self):  # 단순 연결 리스트 생성자
        self.head = None  # 리스트의 첫 번째 노드를 가리키는 head 초기화
        self.size = 0     # 리스트에 있는 노드의 개수 초기화

    def get_size(self):  # 리스트 크기를 반환하는 메서드
        return self.size  # 노드의 개수 반환

    def is_empty(self):  # 리스트가 비어 있는지 확인하는 메서드
        return self.size == 0  # 노드의 개수가 0이면 True, 아니면 False 반환

    def insert_front(self, item):  # 리스트 맨 앞에 새 노드 삽입 메서드
        self.head = self.Node(item, self.head)  # 새 노드를 head 앞에 삽입
        self.size += 1  # 노드 개수 증가

    def insert_after(self, item, p):  # 주어진 노드 p 뒤에 새 노드 삽입
        if p is not None:  # p가 None이 아닌 경우에만 실행
            p.next = self.Node(item, p.next)  # 새 노드를 p 다음에 연결
            self.size += 1  # 노드 개수 증가

    def delete_front(self):  # 리스트의 첫 번째 노드를 삭제하는 메서드
        if self.is_empty():  # 리스트가 비어 있으면 삭제 불가능
            raise EmptyError("Underflow")  # 예외 발생
        self.head = self.head.next  # head를 다음 노드로 변경하여 첫 노드 삭제
        self.size -= 1  # 노드 개수 감소

    def delete_after(self, p):  # 주어진 노드 p 다음의 노드를 삭제하는 메서드
        if self.is_empty() or p.next is None:  # 리스트가 비어있거나 p의 다음 노드가 없으면 실행 불가
            raise EmptyError("Underflow")  # 예외 발생
        p.next = p.next.next  # p의 다음 노드를 건너뛰어 연결하여 삭제
        self.size -= 1  # 노드 개수 감소

    def search(self, target):  # 주어진 값(target)을 가진 노드의 위치를 찾는 메서드
        p = self.head  # 리스트의 첫 노드부터 검색 시작
        index = 0  # 현재 노드의 인덱스 (위치) 초기화
        while p:  # p가 None이 아닐 때까지 반복
            if target == p.item:  # 현재 노드의 값이 target과 같으면
                return index  # 현재 인덱스 반환
            p = p.next  # 다음 노드로 이동
            index += 1  # 인덱스 증가
        return None  # target을 찾지 못하면 None 반환

    def print_list(self):  # 리스트의 모든 노드를 출력하는 메서드
        p = self.head  # 첫 번째 노드부터 시작
        while p:  # p가 None이 아닐 때까지 반복
            print(p.item, end='')  # 현재 노드의 값 출력
            p = p.next  # 다음 노드로 이동
            if p:  # 다음 노드가 있으면
                print(" -> ", end='')  # 화살표 출력
        print()  # 마지막 줄 바꿈

class EmptyError(Exception):  # 리스트가 비어 있을 때 발생할 예외 클래스 정의
    pass  # 빈 클래스, 메시지만 전달
