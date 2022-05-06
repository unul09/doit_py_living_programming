
def service_price():
    service = input('서비스 종류를 입력하세요, a/b/c : ')
    valueAdded = input('부가세를 포함합니까? y/n : ')
    if service == 'a': result = 23
    elif service == 'b': result = 40
    elif service == 'c': result = 67

    if valueAdded == 'y': result = result*1.1

    print(round(result, 1), '만 원입니다.')


service_price()