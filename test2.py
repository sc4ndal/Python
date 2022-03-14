# 1에서 10까지 더하기

sum = 0
for i in range(2,11,2): # 1에서11앞까지
    sum += i
    # sum = sum + i
    # print("i +", i , "=", sum)
    print(i, "+", sum - i, "=", sum)
print("total =", sum)

'''
여러줄
주석
하기
.
'''
# +\를 뒤에 붙이면 뒷 내용을 같은 줄에 표기
data = 'hello ' +\
    'python ' +\
    'happy'
print(data)