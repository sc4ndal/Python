fruit={'사과':'100원','바나나':'200원','수박':'5000원'}
print(fruit.keys())
print(fruit.values())
print(fruit.items())
for i,j in fruit.items():
    print(f'{i}->{j}')
print('------------------')
for i in fruit:
    print(f'{i}->{fruit[i]}')
print(fruit['사과'])