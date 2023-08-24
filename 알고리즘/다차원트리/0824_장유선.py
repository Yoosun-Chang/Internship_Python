# Point 클래스
class Point:
    def __init__(self, x, y):
        self.x = x  # x 좌표
        self.y = y  # y 좌표

# Rectangle 클래스
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x  # 사각 영역의 중심 x 좌표
        self.y = y  # 사각 영역의 중심 y 좌표
        self.w = w  # 사각 영역의 가로 크기
        self.h = h  # 사각 영역의 세로 크기

    def contains(self, point):
        # 주어진 점이 사각 영역 내에 있는지 확인
        return (self.x - self.w <= point.x <= self.x + self.w and
                self.y - self.h <= point.y <= self.y + self.h)

    def intersects(self, other):
        # 다른 사각 영역과 현재 사각 영역이 교차하는지 확인
        return not (other.x - other.w > self.x + self.w or
                    other.x + other.w < self.x - self.w or
                    other.y - other.h > self.y + self.h or
                    other.y + other.h < self.y - self.h)

# QuadTree 클래스
class QuadTree:
    def __init__(self, boundary, capacity):
        """
        QuadTree 생성
        boundary: 현재 노드의 영역을 나타내는 Rectangle 객체
        capacity: 노드에 저장할 수 있는 최대 점의 개수
        """
        self.boundary = boundary  # 현재 노드의 영역 (x, y, w, h)
        self.capacity = capacity  # 노드에 저장할 수 있는 최대 점의 개수
        self.points = []          # 현재 노드에 저장된 점들
        self.divided = False      # 노드가 분할되었는지 여부

    def subdivide(self):
        """
        현재 노드를 4개의 하위 노드로 분할하는 메서드
        """
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h
        half_w = w / 2
        half_h = h / 2
        ne = Rectangle(x + half_w, y - half_h, half_w, half_h)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - half_w, y - half_h, half_w, half_h)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + half_w, y + half_h, half_w, half_h)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - half_w, y + half_h, half_w, half_h)
        self.southwest = QuadTree(sw, self.capacity)
        self.divided = True

    def insert(self, point):
        """
        점을 Quad Tree에 삽입하는 메서드
        point: 삽입할 점을 나타내는 Point 객체
        return: 삽입에 성공하면 True, 실패하면 False를 반환
        """
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()
            if (self.northeast.insert(point) or
                self.northwest.insert(point) or
                self.southeast.insert(point) or
                self.southwest.insert(point)):
                return True

    def get(self, range, found=None):
        """
        주어진 범위 내의 모든 점을 검색하는 메서드
        range: 검색할 범위를 나타내는 Rectangle 객체
        found: 검색된 점을 저장할 리스트 (재귀 호출 시 사용)
        """
        if found is None:
            found = []

        if not self.boundary.intersects(range):
            return found
        else:
            for p in self.points:
                if range.contains(p):
                    found.append(p)
            if self.divided:
                found = self.northwest.get(range, found)
                found = self.northeast.get(range, found)
                found = self.southwest.get(range, found)
                found = self.southeast.get(range, found)

        return found
        
# 두 점 사이의 유클리드 거리를 계산
def calculate_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

import time
import random
import math

# 1. 랜덤으로 -1024, -1024, +1024, +1024 범위의 점 10,000개 생성
points_list = [Point(random.uniform(-1024, 1024), random.uniform(-1024, 1024)) for _ in range(10000)]

# 중심점과 거리 설정
center = Point(127, 37)
radius = 50

# 2. 리스트
# 점 개수 검색 및 시간 측정
start_time_l = time.time()
count_l = 0
for point in points_list:
    if calculate_distance(center, point) <= radius:
        count_l += 1
end_time_l = time.time()
elapsed_time_l = end_time_l - start_time_l

print(f"리스트에 저장된 점의 개수: {len(points_list)}")
print(f"({center.x}, {center.y})에서 거리 {radius}인 점의 개수: {count_l}")
print(f"소요 시간: {elapsed_time_l}초")

# 3. Quad Tree
quad_tree = QuadTree(Rectangle(0, 0, 2048, 2048), 16)
# 점 삽입
for point in points_list:
    quad_tree.insert(point)

# 점 개수 검색 및 시간 측정
start_time_QT = time.time()
points_in_range = quad_tree.get(Rectangle(center.x, center.y, radius, radius))
count_QT = len(points_in_range)
end_time_QT = time.time()
elapsed_time_QT = end_time_QT - start_time_QT
print("==================================================")
print(f"쿼드트리에 삽입된 점의 개수: {len(points_list)}")
print(f"({center.x}, {center.y})에서 거리 {radius}인 점의 개수: {count_QT}")
print(f"소요시간: {elapsed_time_QT}초")