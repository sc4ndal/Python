data = {
    "철수":98,
    "영희":80,
    "순이":100,
    "돌이":70
}
sum = 0
for i,j in data.items():
    sum+=j
    print(f'{i}      {j}')

average = sum/len(data)
print(f'         {average}')

aa=[10,20,30,40]
print(aa.count(40)) #중복 갯수 확인
aa.append(70)
aa.insert(2,80)
print(aa)
print(aa[4])
for i in aa:
    print(f'{aa.index(i)}->{i}')
for i in range(0,10):
    aa.append(0)
print(aa)
print(aa[3])
del(aa[3])
print(aa)