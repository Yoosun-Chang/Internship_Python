import time
import random

# 전체집합
full_set = list(range(1, 1000001))

# 부분집합 생성 함수 정의
def generate_random_subset(count, source_set):
    subset = set()  # 빈 집합
    while len(subset) < count:  # 원하는 개수만큼 원소가 추가될 때까지 반복
        index = random.randint(0, len(source_set) - 1)  # 무작위 인덱스를 선택
        element = source_set.pop(index)  # 선택한 인덱스의 원소를 전체집합에서 뽑는다
        subset.add(element)  # 부분집합에 추가
    return subset

# 부분집합 생성
subset1 = generate_random_subset(700000, full_set.copy())  
subset2 = generate_random_subset(700000, full_set.copy())

start_time = time.time()  # 시작 시간 기록

# 합집합, 교집합, 차집합 계산
union_set = subset1.union(subset2)  # 두 부분집합의 합집합
intersection_set = subset1.intersection(subset2)  # 두 부분집합의 교집합
difference_set = subset1.difference(subset2)  # 첫 번째 부분집합에서 두 번째 부분집합을 뺀 차집합

end_time = time.time()  # 종료 시간 기록

# 결과 출력
print("합집합 개수:", len(union_set))
print("교집합 개수:", len(intersection_set))
print("차집합 개수:", len(difference_set))
print("실행 시간:", end_time - start_time, "초")
