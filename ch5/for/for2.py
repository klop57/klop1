# range:연속된 숫자를 만들어주는 함수
# 반환값: 숫자를 담고 있는 ragne객체
nums = range(10,21) #개수
print(nums)
# 사용방법
for n in nums:
    print(n)

# 0부터 9까지 연속된 숫자 10개를 반환
nums = range(10)
# range 이용해 "안녕하세요" 10번 출력
# range의 값이 필요하지 않은 경우

for _  in nums:
    print("안녕하세요")

# input : 키보드를 통해 값을 입력 받는 함수
num = input() # 사용자가 값을 입력할때까지 대기
print(['입력박은 값:' , num])

# 숫자를 3개 입력받고 합 구하기
sum = 0
num1 = input()
sum = sum + int(num1)
num2 = input()
sum = sum + int(num2)
num3 = input()
sum = sum + int(num3)

# str => int
sum = int(num1) + int(num2) +int(num3)
print

# 반복문으로 숫3개 입력받고 합구하기

# for n in range(3):
#     num = input()
#     sum = sum = int(num)


# i=0
# while i<3:
#     pass
#     i+=1

# for문 안에서 break와 continue 쓰기
# for문으로 1~20까지 합 구하기
sum = 0
for i in range(1,21):
    if sum > 100:
        break
    sum = sum + i
print(sum)

# for문에서 continue 사용하기

for i in range(1,11):
    if i%2 ==1:
        continue
    print(i)
