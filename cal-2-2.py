#함수정의 한 후 반드시 함수 호출
#더하기 함수 정의
def add(a, b):
    c=a+b
    return c
#뺄셈 함수 정의
def minus(a, b):
    c=a-b
    return c
#곱하기 함수 정의
def multi(a,b):
    c=a*b
    return c
#나누기 함수 정의
def divide(a,b):
    c=a/b
    return c

while True:
    a= input('첫번째 숫자를 입력하세요:')
    
    if a == '0000':
        break
    b= int(input('두번째 숫자를 입력하세요:'))
    a= int(a);
    #더하기 함수 호출
    result=a+b
    print(a, '+', b, '=', result)
    #빼기 함수 호출
    result=a-b
    print(a, '-', b, '=', result)
    #곱하기 함수 호출
    result=a*b
    print(a, '*', b, '=', result)
    #나누기 함수 호출
    result=a/b
    print(a, '/', b, '=', result)

print("exit")

