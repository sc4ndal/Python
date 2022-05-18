def genFunc(num):
    for i in range(1,num):
        yield i
        print('제너레이터 진행 중')
for data in genFunc(5):
    print(data)


