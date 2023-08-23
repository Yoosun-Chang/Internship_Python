while True: #유효한 값이 입력될때까지 무한 루프
    try: #예외처리 시작
        first_input = input("첫번째 값: ") #입력
        second_input = input("두번째 값: ") #입력

        if int(second_input) == 0: #두번째 입력값을 정수로 변환하여 0과 비교
            print("0으로 나눌 수 없습니다.") #예외처리
            continue

        result_output = int(first_input) / int(second_input) #나누기 연산을 수행
        print("계산된 값:", result_output) #계산 결과를 출력
        break #정상적으로 계산과 출력이 완료되면 무한 루프를 종료

    except ValueError: #ValueError 예외상황 처리
        print("숫자를 입력하여 주십시오.")
