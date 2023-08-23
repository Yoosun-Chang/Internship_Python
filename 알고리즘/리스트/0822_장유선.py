import time

# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결 리스트 클래스 정의
class Single_LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

# Python 내장 리스트와 연결 리스트 초기화
py_list = []
linked_list = Single_LinkedList()

# Python 내장 리스트
start_time = time.time()
for i in range(100000):
    py_list.insert(0, i)
end_time = time.time()
py_list_time = end_time - start_time

# Single Linked List
start_time = time.time()
for i in range(100000):
    linked_list.insert(i)
end_time = time.time()
linked_list_time = end_time - start_time

print(f"Python 내장 리스트에 데이터를 삽입하는 데 걸린 시간: {py_list_time} 초")
print(f"Single Linked List에 데이터를 삽입하는 데 걸린 시간: {linked_list_time} 초")
