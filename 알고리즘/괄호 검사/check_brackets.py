def check(file_path):
    opening = "([{"
    closing = ")]}"
    stack = []  
    line_number = 0 
    col_number = 0  

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1
                col_number = 0
                for char in line:
                    col_number += 1
                    if char in opening:
                        stack.append((char, line_number, col_number))
                    elif char in closing:
                        if not stack:
                            print(f"Error (line {line_number}, col {col_number})")
                            return
                        top = stack.pop()
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
        print(f"File not found: {file_path}")

    while stack:
        top = stack.pop()
        print(f"Error (line {top[1]}, col {top[2]}): Unmatched openinging bracket '{top[0]}'")

    if not stack:
        print("Pass")

test1_path = "C:\\Users\\inavi\\Desktop\\장유선\\개발교육\\알고리즘\\괄호 검사\\test1.cpp"
test2_path = "C:\\Users\\inavi\\Desktop\\장유선\\개발교육\\알고리즘\\괄호 검사\\test2.cpp"
test3_path = "C:\\Users\\inavi\\Desktop\\장유선\\개발교육\\알고리즘\\괄호 검사\\test3.cpp"


print("Test 1:")
check(test1_path)

print("\nTest 2:")
check(test2_path)

print("\nTest 3:")
check(test3_path)
