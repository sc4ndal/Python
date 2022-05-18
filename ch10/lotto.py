from random import *

lotto=[]

while len(lotto)<6:
    r = randrange(1,46)
    if r not in lotto: #안에 포함돼있지 않으면
        lotto.append(r)

print(sorted(lotto))
lotto.sort()
for i in range(len(lotto)):
    print(lotto[i],end=" ")