# 조건문 만들기

# 조건은 날씨
weather = '눈' # 맑음, 비, 눈

# if~else
# 조건을 만족하면 if블록, 아니면 else블록이 수행됨

# 앞에 조건이 참이면, 다음 조건을 판단하지 않는다
# 모든 조건이 거짓이면 , else 블록을 수행
if weather == '비':
   print("우산을 가져간다")
elif weather == '눈':
   print("장화를 신는다")
else:
   print("우산을 가져가지 않는다")
