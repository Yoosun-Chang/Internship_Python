# 1. 모든 Case를 다 계산
def solve1(weight_limit, weights, values):
    n = len(weights)  
    max_value = 0  

    for i in range(2 ** n):
        combination = []  
        total_weight = 0 
        total_value = 0  

        for j in range(n):
            if (i >> j) & 1: 
                combination.append(j)  
                total_weight += weights[j]
                total_value += values[j]

        if total_weight <= weight_limit and total_value > max_value:
            max_value = total_value 

    print("1번 - 최대 가치:", max_value)

# 2. 다이나믹 프로그래밍
def solve2(limit, w, v):
    n = len(w) 
    table = [0] * (limit+1)

    for i in range(n):

        if w[i] > limit:
            continue

        for j in range(limit, 0, -1):
            if j + w[i] <= limit and table[j] != 0:
                table[j+w[i]] = max(table[j+w[i]], table[j] + v[i])

        table[w[i]] = max(table[w[i]], v[i])

    print("2번 - 최대 가치:", max(table))

# 입력값
limit = 7  
w = [6, 4, 3, 5]  
v = [13, 8, 6, 12] 
solve1(limit, w, v)
solve2(limit, w, v)

