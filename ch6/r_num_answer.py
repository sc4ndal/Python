# import random
#
# tries = 10
# guess = 0
# answer = random.randint(1,100)
#
# print('1부터 100 사이의 숫자를 맞추시오. 도전 기회 10번')

# while guess != answer:
#     guess = int(input("숫자를 입력하세요 : "))
#     tries = tries - 1
#     if (tries != 0):
#         if guess == answer:
#             print("\n정답입니다. 남은 횟수 : ",tries)
#         elif guess < answer:
#             print("그보다 높습니다. 남은 횟수 : ",tries)
#         elif guess > answer:
#             print("그보다 낮습니다. 남은 횟수 : ",tries)
#     else:
#         print('\n실패! 정답은 =',answer)
#         break

for i in ['banana','mango','apple']:
    print(i.index(i),i)