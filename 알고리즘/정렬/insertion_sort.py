def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

        # 정렬 과정을 출력
        #print(f"Step {i}: {arr}")
        
    return arr

print("삽입 정렬 구현을 확인합니다.")
arr = [5, 1, 3, 7, 2, 9]
print("원래 배열:", arr)
sorted_arr = insertion_sort(arr)
print("정렬된 배열:", sorted_arr)

import random
import time

#1번
arr1 = [random.randint(1, 100000) for _ in range(100000)]
start_time = time.time()
insertion_sort(arr1)
end_time = time.time()
print(f"100,000개의 임의 값 정렬 시간: {(end_time - start_time)/60} 분")

#2번
arr2 = list(range(1, 100001))
start_time = time.time()
insertion_sort(arr2)
end_time = time.time()
print(f"1부터 100,000까지의 값 정렬 시간: {end_time - start_time} 초")