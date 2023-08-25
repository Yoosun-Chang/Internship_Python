def insertion_sort(arr):

    n = len(arr)

    #정렬을 수행할 인덱스 설정, 처음은 1
    for i in range(1, n):
        # 현재 원소를 임시로 저장
        temp = arr[i]
        # 현재 원소의 이전 위치를 가리키는 인덱스를 설정
        j = i - 1

        # 현재 원소를 정렬된 위치에 맞게 삽입
        while j >= 0 and arr[j] > temp:
            # 현재 원소보다 큰 값을 오른쪽으로 한 칸 이동
            arr[j + 1] = arr[j]
            # 인덱스 j를 하나 감소시켜 앞쪽의 원소와 비교
            j -= 1

        # 현재 원소를 정렬된 위치에 삽입
        arr[j + 1] = temp

        # 정렬 과정을 출력합니다.
       # print(f"Step {i}: {arr}")

    return arr

print("삽입 정렬 구현을 확인합니다.")
arr = [5, 1, 3, 7, 2, 9]
print("원래 배열:", arr)
sorted_arr = insertion_sort(arr)
print("정렬된 배열:", sorted_arr)


import random
import time

#1번
# 임의의 100,000개의 값을 지니는 리스트 생성
arr1 = [random.randint(1, 100000) for _ in range(100000)]

start_time = time.time()
insertion_sort(arr1)
end_time = time.time()

print(f"100,000개의 임의 값 정렬 시간: {(end_time - start_time)/60} 분")

#2번
# 1부터 100,000까지의 값을 지니는 리스트 생성
arr2 = list(range(1, 100001))

start_time = time.time()
insertion_sort(arr2)
end_time = time.time()

print(f"1부터 100,000까지의 값 정렬 시간: {end_time - start_time} 초")
