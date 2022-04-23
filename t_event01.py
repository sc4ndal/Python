import turtle as t
import random


#global col리스트 생성
col = ['red','yellow','green','blue','white','black','orange','pink'] #0부터 들어가서 0번째는 red 1번째는 yellow 2번째는 green

#주석은 ctrl + / 또는 ''' ~ '''
'''
# print(col)
# print(col[0], col[1], col[7])
# print('length =', len(col)) #총길이 8
# print(type(col))
'''

def fxn(x, y):
    print('x =', x, 'y =', y)
    print('button click')
    # col = ['white','white','white']
    global col #바깥에 있는 col을 불러옴
    ind = random.randint(0, 7)
    t.bgcolor(col[ind])

t.setup(600, 300)  #실행 윈도우 크기
t.screensize(600, 300, 'black')  #내부 캔버스 크기, 배경색

t.onscreenclick(fxn ,1)

t.done()