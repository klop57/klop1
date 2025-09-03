shopping = ["우유", "빵","달걀"]
#  "사과" 추가
#  두번째 요소(빵)를 "치즈"로 수정
#  "우유"삭제
shopping.append("사과")
shopping[1] = "치즈"
shopping.remove("우유")
print(shopping)

scores = [60,75,80,90]
# 100추가
# 세번째 요소를 85 수정
# 마지막 요소 꺼내면 삭제

scores.append(100)
scores[2] = 85
l = scores.pop()
print (scores,l)

animals = ["강아지","고양이","토끼","햄스터"]
# "고양이"를 "고슴도치"로 수정
# 첫번쨰 요소 삭제
# 마지막요소 꺼내면서 삭제
animals[1] = "고슴도치"
del animals[0]
l = animals.pop()
print(animals,l)
print(animals)