sum = 0
while True:
    selection = int(input("1:eval,2:sum,3:exit ''' please select"))
    if  int(selection) == 1 :
        t = input("수식 입력 : ")
        print(eval(t))
    elif int(selection) == 2 :
        x = int(input("***첫번째 숫자 입력 : "))
        y = int(input("***두번째 숫자 입력 : "))
        for i in range(x, y+1) :
            sum += i
        print(f"{x}+...+{y}는 {sum}입니다.")
        sum=0
    else:
        print("exit")
        break