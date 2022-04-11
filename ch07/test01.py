fruit = {'apple':'100원','banana':'50원','melon':'300원'}
print(fruit['apple'])
print('---------')
for i in fruit:
    print(fruit[i])
print('---------')
for i in fruit:
    print(i)
print('---------')
fruit['watermelon']='500원'
fruit['lemon']='30원'
fruit['apple']='5000원'
for i in fruit:
    print(f'{i}->{fruit[i]}')
# print(fruit.keys())
# print(list(fruit.keys()))
# print(fruit.values())
# print(fruit.items())
# print('fruit.item')
# for i,j in fruit.items():
#     print(i,'=>',j)
