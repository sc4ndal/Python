money, c500, c100, c50, c10 = 0,0,0,0,0

while True:
    money=input('교환할 돈 : ')
    # money_string = str(money)
    if money == '0000' :
        print('exit program')
        break
    money = int(money)
    c500=money//500
    money %= 500
    c100=money//100
    money %= 100
    c50 = money // 50
    money %= 50
    c10 = money //10
    money %= 10

    print('\n500원짜리 - %d개'% c500)
    print('100원짜리 - %d개'% c100)
    print('50원짜리 - %d개'% c50)
    print('10원짜리 - %d개'% c10)
    print('남은 잔돈 - %d원\n'% money)
