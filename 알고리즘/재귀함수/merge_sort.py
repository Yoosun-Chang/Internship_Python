import random

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = [] 
    i, j = 0, 0  

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j]) 
            j += 1

    result += left[i:]
    result += right[j:]

    return result

random_list = [random.randint(0, 1000000) for _ in range(100000)]
sorted_list = merge_sort(random_list)
print("정렬된 배열의 처음 10개 값:", sorted_list[:10])
print("정렬된 배열의 마지막 10개 값:", sorted_list[-10:])
