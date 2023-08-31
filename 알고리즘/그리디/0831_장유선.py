def greedy(change, coin_list):

    counts = {}
    
    # 최소 동전 개수를 계산
    for coin in sorted(coin_list, reverse=True):
        coin_count = change // coin
        
        if coin_count > 0:
            counts[coin] = coin_count
            change -= coin * coin_count
    

    result = []
    
    for coin, count in counts.items():
        result.append(f"{coin}*{count}")
    
    return f"{sum(counts.values())} ({', '.join(result)})"

# 입력값과 동전 종류
change1 = 63
coin_list1 = [1, 5, 10, 25]
change2 = 15
coin_list2 = [1, 2, 5, 10]
change3 = 6
coin_list3 = [1, 3, 4]

# 결과 출력
print(greedy(change1, coin_list1))  
print(greedy(change2, coin_list2))
print(greedy(change3, coin_list3)) 
