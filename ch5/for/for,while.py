# 반복문:while for
# while: 조건이 참인 동안 반복 수행
# for: 자료구조에서 요소를 하나씩 꺼내면서 반복 수행

lis = ['a','b','c','d','e']
# 리스트의 크기만큼 반복 수행
for ch in lis:
    print(ch)
# 딕셔너리 생성
dic = {'apple':1200,'banana':800,'orange':1500}

# for문으로 딕셔너리 안에 요소 하나씩 꺼내기
for k in dic:
    print(k)

# 값 꺼내기
print(dic.values())
# for 변수 in 리스트,튜플,딕셔너리,iter
# iterable(이터러블: 순회가 가능한 객체
for v in dic.values():
    print(v)

# dic.items: 키,값 모두 가지고 있는 객체
# dict_items(['apple':1200,'banana':800,'orange':1500])
# 튜플 구조 분해로 값을 하나씩 변수에 대입.
for key, value in dic.items():
    print(key,value)

# range : 연속된 숫자를 만드는 객체
# range(개수)
print(range(10))

# range는 이터러블 객체
for n in range(10):
    print(n)

for n in range(1,11):
    print(n)
# 안녕하세요 10번 출력
# n 변수 사용 안함 => 변수 생략 사능
for _ in range(10):
    print("안녕하세요")

# for문을 사용해 전체 평균 점수를 구하세요
scores = {"철수":80, "영희": 95,"민수":70, "지연":100}
sum = 0

for value in scores.values():
    sum = sum + value
print(sum)

#학생의 수 구하기
size = (len(scores))

# 평균 구하기
avg = sum / size
print(avg)

# 퍼플렉시티 답
# values는 이터러블로 for문 사용 가능
scores = {"철수":80, "영희": 95,"민수":70, "지연":100}
sum = 0

for value in scores.values():
    sum += value

average = sum / len(scores)
print(average)

# 90점 이상 학생의 수를 구하세요
scores = {"철수":80, "영희": 95,"민수":70, "지연":100}
cnt = 0

for value in scores.values():
    if value >= 90: #학생의 점수와 90점을 비교
        cnt = cnt + 1
print(cnt)

# 리스트 생성
nums = [1,2,3,4]
# 새로운 리스트 생성
new_nums = []

# nums를 사용해 새로운 리스트 생성
# nums의 각 요소에 *3을 해서 [3,6,9,12]만들기

for n in nums:
    new_nums.append(n*3)

# 위 코드를 '리스트 컴프리헨션'이라는 문법으로
# 간단하게 작성하기!
# 새로운 리스트 = [변수 + 반복문]
new_nums = [ n*3 for n in nums]
print(new_nums)

# list 생성
nums = [1,2,3,4,5,6,7,8,9,10]
# nums를 사용해 새로운 리스트 만들기
new_nums = []
# nums에서 짝수만 골라서 new_nums에 담기
for n in nums:
    if n%2 == 0:
        new_nums.append(n)
print(new_nums)

#위 코드를 '리스트 컴프리헨션' 문법으로 바꾸기
# 새로운 리스트 = [변수 + for + if]
new_nums = [n for n in nums if n%2 == 0]

# 리스트 생성
strings = ['a','bb','ccc','dddd','e']
# strings을 사용해 새로운 리스트 생성
new_str = []
# 문자열 리스트에서 문자의 크기가 2보다 큰 것을 찾고
# 대문자로 변환해서 new_str에 담기

for ch in strings:
    if len(ch) > 2:
        new_str.append(ch.upper())
print(new_str)

# '리스트 컴프리헨션'으로 작성
new_str =[ ch.upper() for ch in strings if len(ch)]