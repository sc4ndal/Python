myList=[1,2,3,4,5]
result1=[]
for val in myList:
    result1.append(val+1)
print(f'result1:{result1}')

def add_one(n):
    return n+1

result2=list(map(add_one,myList))
print(f'result2:{result2}')