f = open('input.txt', 'r', encoding='utf-8')
lines = f.read().splitlines()

data = []
count = 0
sum = 0

for line in lines:
    num = line.strip('\ufeff')
    num = int(num)
    data.append(num)
    sum += num

    if num <= 30000:
        count += 1

    minimum = min(data)
    maximum = max(data)
    avg = sum / len(data)

    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(f"30000 이하의 값: {count}개\n")
        f.write(f"최소값: {minimum}\n")
        f.write(f"최대값: {maximum}\n")
        f.write(f"평균: {avg:.6f}\n")

with open('result.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

for line in lines:
    print(line)