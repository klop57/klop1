# # 키보드로 값 입력받기

# # a = input()
# # print(a)

# b = input('숫자를 입력하세요:')
# print('입력받은 값:',b)

# n1 = input('첫번째 숫자를 입력하시오:')
# n2 = input('두번째 숫자를 입력하시오:')
# sum = int(n1) + int(n2)
# print('결과:', sum)

# # n1,n2 자료형 확인
# print(type(n1),type(n2))

# n1 = input('첫번째 숫자를 입력하시오:')
# n2 = input('두번째 숫자를 입력하시오:')
# sum = int(n1) * int(n2)
# print('결과:', sum)

def sub(name,age):
    print(f'{name}님의 나이는 {age}세 입니다')

result = sub("둘리",7)
print(result)


# def sub(price,cnt):
#     sum = price * cnt
#     return sum
   
# result = sub(1500,5)
# print(result)

# price = input("사과 가격:")
# cnt = input("사과 개수:")
# sum = int(price) * int(cnt)
# print(sum)

# score = input ("몇점인가요? :")
# if int(score) >= 60 :
#     print ("합격")
# else :
#     print ("불합격")


# age = input ("몇살이세요? :")
# if int(age) <= 12:
#     print (1000)
# elif int(age) <= 18:
#     print (1500)
# else :
#     price(2000)

while True:
    text = input("입력하세요 :")
    if text == '0' :
        print("종료합니다")
        break

# 키보드로 입력
# 모니터로 출력
# print : 화면에 숫자,문자,리스트 등을 출력하는 함수

print(123)
print('abc')
print([1,2,3]) 

# 여러 문자열 연결해서 출력하기
print('hello' 'world')
print('hello' + 'world')
print('hello' ,'world')


# print 함수의 특징
print(1)
print(2)
print(3)

# print 함수의 선업부
# end는 기본값이 있는 매개변수
# '\n'는 특수문자로 줄바꿈 가능
# end 옵션은 앞에 value를 출력하고, 마지막으로 \n을 출력함
# print(value, end= '\n')

# end 매개변수를 줄바꿈 대신 공백으로 바꾸기
print(1, end=' ')
print(2, end=' ')
print(3, end=' ')