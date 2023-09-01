def check(file_path):
    opening = "([{"
    closing = ")]}"
    stack = [] 
    line_number = 0  # 현재 라인 번호
    col_number = 0  # 현재 열 번호

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1
                col_number = 0
                for char in line:
                    col_number += 1
                    if char in opening:
                        # 여는 괄호일 경우 스택에 추가 
                        stack.append((char, line_number, col_number))
                    elif char in closing:
                        # 닫는 괄호일 경우
                        if not stack:
                            # 여는 괄호가 없는데 닫는 괄호가 나온 경우, 에러 출력 후 함수 종료
                            print(f"Error (line {line_number}, col {col_number})")
                            return
                        top = stack.pop()
                        # 괄호 쌍이 일치하지 않는 경우, 에러 출력 후 함수 종료
                        if top[0] == '(' and char != ')':
                            print(f"Error (line {top[1]}, col {top[2]})")
                            return
                        if top[0] == '[' and char != ']':
                            print(f"Error (line {top[1]}, col {top[2]})")
                            return
                        if top[0] == '{' and char != '}':
                            print(f"Error (line {top[1]}, col {top[2]})")
                            return
                        
                        top = []

    except FileNotFoundError:
        # 파일을 찾을 수 없는 경우 에러 출력
        print(f"File not found: {file_path}")

    # 남은 여는 괄호 처리
    while stack:
        top = stack.pop()
        # 여는 괄호가 닫히지 않은 경우, 에러 출력
        print(f"Error (line {top[1]}, col {top[2]})")

    # 모든 괄호가 정상적으로 닫혔는지 확인하고 결과 출력
    if not stack:
        print("Pass")  # 스택이 비어있으면 괄호가 모두 정상적으로 닫혔음을 의미

# 파일 경로 설정
test1_path = "C:\\Users\\inavi\\Desktop\\장유선\\개발교육\\알고리즘\\괄호 검사\\test1.cpp"
test2_path = "C:\\Users\\inavi\\Desktop\\장유선\\개발교육\\알고리즘\\괄호 검사\\test2.cpp"
test3_path = "C:\\Users\\inavi\\Desktop\\장유선\\개발교육\\알고리즘\\괄호 검사\\test3.cpp"

# 테스트 실행
print("Test 1:")
check(test1_path)

print("\nTest 2:")
check(test2_path)

print("\nTest 3:")
check(test3_path)
