# 다음과 같이 딕셔너리를 만들고 
# for문으로 key를 하나 출력
students = {"이름":"둘리","나이":20,"주소":"인천"}
for key in students:
    print(key)

# 다음과 같이 딕셔너리를 만들고
# for문으로 value를 하나씩 출력
coffee_menu = {"아메리카노": "2500원","라떼": "3000원", "케이크": "4500원"}

for value in coffee_menu.values():
    print(value)

# for문을 사용해서 11부터 20까지 출력
for n in range(11,21):
    print(n)

# for문을 사용해서 5부터 15까지 출력
for n in range(5,16):
    print(n)
# for문을 사용해서 "hi" 5번 출력
for _ in range(5):
    print("hi")

nums = [10,20,30,40,50]
sum = 0
# for문으로 모든 요소를 더해서 합을 구하세요
for n in nums:
    sum += n
print(sum)

# for문을 사용해서
# 1~100까지 숫자 중에서 3의 배수 출력
for n in range(1,101):
    if n%3 == 0:
        print(n)

# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 *별을 출력
# 예) n=5 => *****
num = 5
print( '*' * num)

# for문 사용
str1 = '' # 결과를 저장할 변수
for _ in range(num):
    str1 = str1 + '*'
print(str1)

# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 삼각형을 그려주세요
# n=5


n = 5  # 숫자 대입

for i in range(1, n + 1):
    print('*' * i)

n =5
for a in range(1, n + 1):
    print((n-a)* ' ','*' * a)

n =5
for a in range(1,6):
    print(' '*(n-a),'*' * a)

# 구구단 중에서 3단을 출력
for i in range(1,10):
    print(f"3 * {i} = {3*i}")
# n =5
# r = range(1,10)
# for n in r:
#     print( n,'x',r,'=',(n))

# 리스트 생성
nums = [5,9,3,8,2]

# 리스트에서 가장 큰 값 구하기 
max = nums[0] 

# 과정 
# 5 9 비교 => 9 (max nums[1])
# 9 3 비교 => 9 (max nums[2])
# 9 8 비교 => 9 (max nums[3])
# 9 2 비교 => 9 (max nums[4])
# 리스트의 요소와 현재 가장 큰 값을 비교
# 가장큰값 max, 리스트의 요소  nums

for n in nums:
    print(n) #5,9,3,8,2
    if max < n:
        max = n
print(max)