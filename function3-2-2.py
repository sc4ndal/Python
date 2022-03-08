a=input('1은더하기,2는빼기,3은곱하기,4는나누기\n사용할 함수를 정해주세요:')
    if a == '1':
        def add(b,c):
        d=b+c
        return d
    sum = add(int(input('첫번째 숫자를 입력하세요:')),int(input('두번째 숫자를 입력하세요:')))
print('sum = ',sum)

break
    
    if a=='2':
        def minus(b,c):
            d=b-c
            return d
        sum = minus(int(input('첫번째 숫자를 입력하세요:')),int(input('두번째 숫자를 입력하세요:')))
print('sum = ',sum)

break   
            if a=='3':
                def multi(b,c):
                    d=b*c
                    return d
                sum = multi(int(input('첫번째 숫자를 입력하세요:')),int(input('두번째 숫자를 입력하세요:')))
print('sum = ',sum)

break           
                    if a=='4':
                        def divide(b,c):
                            d=b/c
                            return d
                        sum = divide(int(input('첫번째 숫자를 입력하세요:')),int(input('두번째 숫자를 입력하세요:')))
print('sum = ',sum)
break
        

