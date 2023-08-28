import random

# 합병 정렬
def merge_sort(lst):
    # 리스트의 길이가 1 이하이면 이미 정렬되어 있는 상태이므로 그대로 반환
    if len(lst) <= 1:
        return lst

    # 리스트를 반으로 나누기 위한 중간 지점 찾기
    mid = len(lst) // 2
    
    # 왼쪽 부분과 오른쪽 부분을 재귀적으로 정렬
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # 정렬된 두 부분을 합병
    return merge(left, right)

# 두 부분 리스트를 합병하는 함수
def merge(left, right):
    result = []  # 결과를 저장할 빈 리스트
    i, j = 0, 0  # 왼쪽과 오른쪽 부분 리스트의 인덱스

    # 두 부분 리스트를 비교하면서 합병
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # 왼쪽 요소를 결과 리스트에 추가
            i += 1
        else:
            result.append(right[j])  # 오른쪽 요소를 결과 리스트에 추가
            j += 1

    # 남은 요소들을 결과 리스트에 추가 (한쪽 부분이 끝까지 갔을 경우)
    result += left[i:]
    result += right[j:]

    return result

# 0부터 1,000,000 범위 내에서 100,000개의 무작위 값 생성
random_list = [random.randint(0, 1000000) for _ in range(100000)]

# 합병 정렬 수행
sorted_list = merge_sort(random_list)

# 결과 출력
print("정렬된 배열의 처음 10개 값:", sorted_list[:10])
print("정렬된 배열의 마지막 10개 값:", sorted_list[-10:])
