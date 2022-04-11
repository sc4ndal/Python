l = ['apple',10,'mango','banana',True,'watermelon']
for i in l:
    # print(l.int[i])
    if 'apple' in l:
        print('buy')
    else:
        print('lack')
    # print(l.index())
print('-----')
print('apple' in l)
print('chherry' in l)
print('-----')
print(len(l))
print(l[0])
l.append('melon')   #맨뒤에 추가
print(l)
print(l.pop())      #맨뒤의 배열 삭제
print(l.pop())
print(l)
# for i in l:
#     print('',i)