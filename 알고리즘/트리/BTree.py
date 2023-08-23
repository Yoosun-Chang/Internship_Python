class BTreeNode:
    def __init__(self):
        self.values = [] 
        self.children = [] 

class BTree:
    def __init__(self):
        self.root = BTreeNode() 

    def insert(self, value):
        self.insert_value(self.root, value)

    def insert_value(self, node, value):
        if not node.children:
            node.values.append(value)
            node.values.sort()

            if len(node.values) > 4:
                left_node = BTreeNode()
                right_node = BTreeNode()
                left_node.values = node.values[:2] 
                right_node.values = node.values[3:]
                node.values = [node.values[2]]
                node.children = [left_node, right_node]

        else: 
            i = 0
            while i < len(node.values):           
                if value < node.values[i]:
                    break
                i += 1
            self.insert_value(node.children[i], value)

    def get(self, value):
        return self.get_value(self.root, value)

    def get_value(self, node, value):
        if not node.children: 
            return value in node.values
        else:
            i = 0
            while i < len(node.values):
                if value == node.values[i]:
                    return True
                if value < node.values[i]:
                    return self.get_value(node.children[i], value)
                i += 1
            return self.get_value(node.children[i], value)

def print_tree(node, level=0):
    if node is not None:
        print(f"Level {level}: {node.values}")
        for child in node.children:
            print_tree(child, level + 1)

btree = BTree()
values_to_insert = [5, 2, 11, 6, 7, 8, 3, 10, 15]
print("[5, 2, 11, 6, 7, 8, 3, 10, 15]를 삽입합니다.")
for value in values_to_insert:
    btree.insert(value)
    
values_to_check = [3, 10, 6]
print("[3, 10, 6]값이 있는지 확인합니다.")
for value in values_to_check:
    found = btree.get(value)
    if found:
        print(f"{value}를 찾았습니다.")
    else:
        print(f"{value}를 찾지 못했습니다.")
print("\nB-Tree 노드와 레벨을 확인합니다.")
print_tree(btree.root)


import random
import time

values_insert = random.sample(range(1000001), 100000)
values_find = random.sample(range(1000001), 10000)

start_time = time.time()
l = []
for value in values_insert:
    l.append(value)
list_insert_time = time.time() - start_time

start_time = time.time()
btree = BTree()
for value in values_insert:
    btree.insert(value)
btree_insert_time = time.time() - start_time

start_time = time.time()
for value in values_find:
    found = value in l
    '''
    if found:
        print(f"{value}를 찾았습니다.")
    else:
        print(f"{value}를 찾지 못했습니다.")
    '''
list_find_time = time.time() - start_time

start_time = time.time()
for value in values_find:
    found = btree.get(value)
btree_find_time = time.time() - start_time

print("\nList와 B-Tree의 소요시간을 출력합니다.")
print(f"List 소요 시간: {abs(list_find_time - list_insert_time)} 초")
print(f"B-Tree 소요 시간: {abs(btree_find_time - btree_insert_time)} 초")

