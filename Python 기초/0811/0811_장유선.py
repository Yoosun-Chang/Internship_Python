def read_dbf_file(file_path):
    with open(file_path, 'rb') as f:
        version = f.read(1)
        year = f.read(1) 
        month = f.read(1)
        day = f.read(1)
        record_number = int.from_bytes(f.read(4), byteorder='little') 
        header_bytes = int.from_bytes(f.read(2), byteorder='little')
        record_bytes = int.from_bytes(f.read(2), byteorder='little')

        f.read(20) #건너뛴다

        #필드 정보 하나당 32바이트를 사용하므로 필드 정보 바이트를 제외한 부분을 
        #필드 정보 하나의 바이트 수로 나누어 필드 개수를 계산
        field_count = (header_bytes - 32 - 1) 
        fields = []

        '''필드 정보의 크기와 내용을 파일에서 읽어와서 field_info, field_type, field_length 변수에 저장한다.
        field_info를 utf-8 형식으로 디코딩하고, 끝에 있는 NULL 바이트('\x00')를 제거한다.
        필드 정보 하나를 읽을 때마다 32바이트를 읽어 건너뛴다.'''

        for _ in range(field_count):
            field_info = f.read(11).decode('utf-8').rstrip('\x00')
            field_type = f.read(1).decode('utf-8')
            f.read(4)  
            field_length = int.from_bytes(f.read(1), byteorder='little')
            f.read(15)  
            fields.append((field_info, field_type, field_length))

        f.read(1) #terminator 건너뛰기

        print("필드 정보")
        for field in fields:
            print("- " + field[0])

        # 데이터 레코드 출력
        for _ in range(record_number):
            f.read(1)  # Skip the record marker
            record_data = f.read(record_bytes - 1) #레코드 마커 바이트를 제외한 나머지 데이터 읽기
            offset = 0 #레코드 데이터에서 각 필드의 시작 위치를 나타내는 변수 초기화
            print('\n')
            print("Row", _ + 1) #현재 처리중인 레코드 번호 출력

            for field_info, _, field_length in fields:
                field_value = record_data[offset:offset + field_length].rstrip(b'\x00').decode('utf-8')
                print(f"- {field_info}: {field_value.strip()}")
                offset += field_length

        '''
        - record_data[offset:offset + field_length]는 레코드 데이터에서 현재 필드의 데이터를 읽는다. offset부터 offset + field_length까지의 데이터를 가져온다.
        - .rstrip(b'\x00')은 읽어온 데이터 뒤에 있는 NULL 바이트를 제거한다.
        - .decode('utf-8')는 바이트 데이터를 UTF-8 문자열로 변환한다.
        - print(f"- {field_info}: {field_value.strip()}")은 현재 필드의 정보와 읽어온 데이터를 출력한다. .strip()을 사용하여 문자열 앞뒤 공백을 제거한다.
        - offset += field_length은 다음 필드의 시작 위치를 업데이트하여 다음 필드를 읽어오기 위한 변수이다. 
        '''
                


# DBF 파일 경로 설정
dbf_file_path = 'sample.dbf'

# DBF 파일 읽기 및 필드 정보 및 레코드 출력
read_dbf_file(dbf_file_path)
