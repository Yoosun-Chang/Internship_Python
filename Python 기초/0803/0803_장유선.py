rows = '''쿠크다스,14232,3400
초코하임 화이트,122,3300
엄마손 파이 딸기맛,123,2800
쿠크다스 귀지맛,43543,2400
초코하임 초코맛,1243,3300
엄마손 파이 유통기한 지난 것,133,1800원'''

for row in rows.split('\n'):
    tokens = row.split(',')
    name = tokens[0]
    stock = tokens[1]
    price = tokens[2]

    if '엄마손 파이' in name and not price.isdigit():
        print(f"{name},{stock},{price}")
