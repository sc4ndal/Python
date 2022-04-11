foods = {
    "떡볶이":"오뎅",
    "자장면":"단무지",
    "라면":"김치",
    "피자":"피클"
}
foods["맥주"]="땅콩"
foods["치킨"]="치킨무"
foods["삼겹살"]="상추"

# while(True):
#     myfoods = input(str(list(foods.keys()))+"중 좋아하는 음식은? ")
#     if myfoods in foods :
#         # print("<%s>궁합 음식은 <%s>입니다." %(myfoods, foods.get(myfoods)))
#         print(f'<{myfoods}>의 궁합 음식은 <{foods.get(myfoods)}>입니다.\n종료하시려면 끝 이라고 적어주세요.')
#     elif myfoods == "끝":
#         break
#     else:
#         print("그런 음식은 없습니다. 확인해주세요.\n종료하시려면 끝 이라고 적어주세요")
# ---------------------------------------
# foods = {}
# foods["떡볶이"] = "오뎅"


# print(foods)

#모든 key 가져오기
# print(foods.keys(),print(foods.values()))

# for key in foods.keys():
    # print(key, foods.get(key))
    # print('------')
    # print("key = ", key, "value = ", foods.get(key))
# print(foods.values())
# print(foods.get("자장면"))

for item in foods.items():
    items = list(item)
    print(list(item))
    items.append("감자")
    print(items)
    print(items.pop())
    print(items)