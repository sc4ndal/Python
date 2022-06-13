def hap(num1,num2):
    res=num1+num2
    return res
print(hap(10,20))

hap2 = lambda x,y:x+y
print(hap2(10,20))

myList=[1,2,3,4,5]
add10=lambda num:num+10
myList = list(map(add10,myList))
print(myList)



