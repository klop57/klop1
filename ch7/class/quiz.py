# math 모듈 가져오기
# math란? 파이썬에서 제공하는 기능 중 하나로
# 수락 함수를 가지고 있음 (abd,sum)

import math


# math 모듈의 ceil(올림)과 floor(내림) 함수 사용
print(math.ceil(3.14))
print(math.floor(3.14))


from math import ceil,floor

ceil(3.14)
floor(3.14)

# random 모듈을 가져와서
# randint(시작,끝)함수로
# 1~6사이의 랜덤 숫자 6개를 뽑으세요

# import random
# print(random.randint(1,6))

# from random import randint
# for _ in range(6):
#     n = randint(1,6)
#     print('1~6중에 랜던한 값:', n)


# # time 모듈을 가져와서 
# # sleep(초) 함수로
# # 2초 동안 기다린 뒤 "끝!"을 출력하세요
# import time
# time.sleep(2)
# print('끝!')

# # os모듈을 가져와서
# # getcwd() 함수로
# # 현재 작업 경로를 출력하세요
# import os
# print(os.getcwd)

# # 파이썬을 개발하다가 자주 만나는 에러

# lis = [1,2,3]

# # 리스트에서 요소 꺼내기
# lis[3]

# 파일열기
# 존재하지 않는 파일을 열면 에러남
# # 'w' 쓰기 모드는 상관없음 생성 해쁜다.
# f = open('a.txt','r')

# 나누는 값이 0이면 에러남


# 위에서 오류가 나면 프로그램이 중간에 종료됨


# 예외처리:오류가 발생해도 프로그램이 멈추지 않고
# 계속 실행할 수 있도록 처리하는 것

# 예외 처리 구조
# try블록 안에서 오류가 발생하면 except 블록이 실행됨
# 오류가 발생하지 않으면 except 블록 실행 안됨

# try:
#     # 에러가 발생할 수 있는 코드
#     4/2
# except IndexError as e:
#     print(e)
# print('프로그램이 정상적으로 종료되었습니다')
    # 에러가 났을 때 처리할 코드

# 실제로 발생되는 에러를 확인 ZeroDivisionError


# lis =[1,2,3]
# lis[3]

# 0/4

# try = finally 구조
# # finally는 오류와 상관없이 항상 실행됨
# f= None

# try:
#     # 에러가 발생할 코드 입력
#     f = open('test.txt','r')
# finally:
#     f.close()
#     print('file close')


# try: 
#     lis =[1,2,3]
#     lis[3]
#     # 4/0
# # except 블록 하나로 에러 여러개 처리하기
# except (IndexError,ZeroDivisionError) as e :
#     print(e)

# # try-excep-else 수조

try:
    age = int(input())
except ValueError as e:
    print("사람의 나이가 정확하지 않습니다")
else:
    # 에러가 발생하지 않으면
    # 프로그램을 이어서 작성
    # 사람의 나이가 18살 이하면 입장 불가
    if age <= 18:
        print('입장 불가!')
    else:
        print('입장 가능~') 

# age = int(input()) #ValueError


# raise : 에러를 강제로 발생시키는 명령

# 먼저 클래스 만들기
# 함수 오버라이드를 강제할때 사용하는 코드
class Bird:
    def fly():
        raise NotImplementedError
    
# bied를 상속받는 자식 클래스
class Eagle(Bird):
    def fly(self):
        print("fly~~")


eagle = Eagle()
eagle.fly()


#파이썬의 함수
# 모듈을 불러와서 사용해야 하는 것: math 등
# 모듈을 불러오지 않고 바로 사용 가능한 것 : print 등

# len : 자료구조의 길이를 구하는 함수
print(len('python'))
print(len([1,2,3]))
print(len((1,'a')))

# max : 제일 큰 값 구하기
print(max([1,5,3,4]))

# min : 제일 작은 값 구하기
print(min([1,5,3,4]))

# round : 반올림. 0.5이상이면 => 1
print(round(4.6))
print(round(4.2))
print(round(5.578,2))

# sort : 리스트를 순차적으로 정렬
print(sorted([3,1,2]))
print(sorted(['a','c','d']))

# reversed : 역순으로 정렬
print(reversed([3,1,2]))

# sum : 합계
print(sum([1,2,3]))


# type : 자료형 확인
print(type(123))
print(type('abc'))
print(type([1,2,3]))

# abs : 절대값 구하기
print(abs(-3))
print(abs(-1.2))

# enumerate : 리스트에 인덱스 붙이기
for i, value in enumerate(['a','b','c']):
    print(i,value)

# zip : 튜플 묶기
t1 = ('a','b','c')
t2 = ('c','d','e')
print(list(zip(t1,t2)))

# 날짜와 시간

# 모듈 불러오기

from datetime import datetime, date, time

# 연도,월,일시,분,초
dt = datetime(2025,9,11,12,38,00)

# 날짜와 시간 꺼내기
print(dt.day)
print(dt.minute)

# 언제 활용할까?
# 상품의 주문시간을 저장
# 사용자가 업로드한 파일을 날짜별로 저장

# 날짜와 시간으로 분리
print(dt.date())
print(dt.time())

# 문자열 => 시간 객체로 변환
# date_str = '20250911'
# # 문자열,포맷
# # 포맷은 왜 필요할까
# # 날짜 = 연도,월,일,시,분,초
# print(datetime.strptime(date_str,'%Y%m&d'))

# 리스트의 최대값과 최소값을 구하세요
# 리스트: [3,1,7,4]
print(max([3,1,7,4]))
print(min([3,1,7,4]))

# 리스트를 정렬하세요
# 리스트: [10,2,33,25]
print(sorted([10,2,33,25]))

print(sum((5,10,15)))

print(abs(-7))
print(abs(-3.14))

print(type('hello'))
print(type([1,2,3]))
print(type(3.14))


# try - except - finally
# f를 try와 finally 모두 사용하기 위해서
# f를 전역 변수로 선언
# 전역변수란? 제일 밖에서 선언되어 모든 곳에서 사용 할수 있는
f=None
try:
    f = open('test.txt', 'r')
except FileExistsError as e:
    print(e)
finally:
    if f == None:
        print('파일이 없습니다')
    else:
        print("파일을 닫았습니다")
        f.close()