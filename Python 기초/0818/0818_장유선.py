import urllib.request

client_id = "ple3eOsgY9FpjI5vJcvZ"
client_secret = "1ftYQ3WCuC"

url = "https://openapi.naver.com/v1/search/local.json"

# 검색어를 입력 후, urllib.parse.quote() 함수를 사용하여 검색어를 URL 인코딩
query = "?query=" + urllib.parse.quote(input("검색어 입력:"))
url_query = url + query # 요청 URL 생성
request = urllib.request.Request(url_query)

request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()

# HTTP 상태 코드가 200인 경우
if rescode == 200:
    # 응답 본문
    response_body = response.read()
    # 응답 본문을 UTF-8 문자열로 디코딩
    print(response_body.decode('utf-8'))
else:
    # HTTP 상태 코드가 200이 아닌 경우 오류 메시지
    print("Error code:" + rescode)
