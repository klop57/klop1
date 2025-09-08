#  더하기 함수 만들기
# def 함수이름 (매개변수): ...
# 매개변수 : 함수에 필요한 입력값 (예를 들어 숫자 2개)
# 반환값 : 결과
def add(a,b):
    return a + b #반환값    

# 함수 사용 (함수 호출)
# f5
sum = add(3,4) # 함수이름(입력값) #f11
print(sum)


# 두 개의 숫자를 입력 받아 곱한 값을
# 반환하는 함수를 작성하고 호출하세요
# 에)  2,5 => 10

def mult(a,b):
    return a * b

result = mult(2,5)
print(sum)

# 인사를 출력하는 함수 만들기
# 입력값 없고, 반환값도 없는 함수
def hello():
    print("안녕하세요")

# 함수 호출
hello()
hello()
hello()
hello()

# 함수의 여러가지 형태
# 함수의 형태에 따라 호출하는 방법 알기
# 입력값도 있고, 리턴값도 있는 함수
# 두 수를 더하는 함수
def add(a,b):
    return a+b
# 함수를 호출 할 때, 두 숫자를 입력하고
# 호출이 끝난 후에, 결과를 받아야함
result = add(3,4)
print(result)



# 입력값도 없고, 리턴값도 있는 함수
# 인사를 반환하는 함수
def say():
    return 'hi'
# 리턴값이 있으면 결과를 받아야함.
string = say()
print(string)

#입력값 있고 , 리턴값은 없는 함수
# 두수를 더하고 결과를 바로 출력하는 함수
# 매개변수,입력값,인자
# 함수를 정의할때는 a와b를 매개변수라고 부른다
def add(a,b):
    print(a+b)
# 매개변수가 있으면 개수에 맞게 입력
# 함수를 호출할때는 3과 4를 인자라고 부르나
add(3,4)

# 이름을 입력받아 환영 인사를 출력하는 함수를 작성하세요
# 예) '둘리' => '둘리님, 환영합니다'
def f(name):
    return("둘리님,환영합니다")
f = ('둘리')
print(f)


# 이름과 인사말을 받아 이름+인사말 형태의 문자열을
# 출력하는 함수를 작성하세요
# 예) '둘리','안녕하세요' => '둘리님, 안녕하세요'
# 예) '또치','hi' => '또치님, hi~~'
# 입력값 : 문자 2개
# 반환값 : 없음

def f(name,msg):
    # 문자열 연결 방법: + , f-str
    print(f'{name}님, {msg}')
# 매개변수가 있으면 개수를 맞춰서 입력값 넣기
f('둘리','안녕하세요')

# 함수 응용하기
# 입력한 숫자만큼 '안녕하세요' 출력하기
# 입력값:반복횟수
def hello(cnt):
    for _ in range(cnt):
        print('안녕하세요')
# 함수 호출
# 매개변수가 있으면 입력값을 넣어서 함수를 호출
hello(10)

# 두 개의 숫자를 입력 받아,
# 1번째 수에서 2번째 수까지의 합을 반환하는 함수를 
# 예) 5,10 => 5+6+7+8+9+10 = 45
# def nums(a,b):
#     sum = 0
#     for _ in range(a,b):
#     sum = sum + 1
# print

# 두 개의 숫자를 입력 받아,
# 첫 번째 수에서  두번째 수를 뺀 결과를 반환하는 함수를 작성
# 단, 첫번째 수가 두번째 수보다 작으면 -999를 반환하세여
# 20, 10 => 10
# 10, 20 => -999

# 함수 이름:내마음대로 ~ func sub 등 
# 입력값: 숫자 2개
# 반환값: 1번째에서 2번째 뺀 결과 및 작을때 결과의 -999
# 그렇지 않으면 계산한 결과를 반환
def sub(n1,n2):
    if n1 < n2:
        return -999
    else:
        return n1 - n2
  
# 함수 호출
result1 = sub(20,10)
print(f' 결과:{result1}')
result2 = sub(10,20)
print(f' 결과:{result2}')

#리턴값 있음 -> 결과를 함수 내부에서 처리하지 않고 반환 받는 쪽에서 처리해야함.


# 함수 내부에서 return 키워드 여러번 사용가능
# 함수 내부에서 return을 한번만 만날 수 있다
def sub(n1,n2):
    if n1 > n2:
        return - 999
    else :
        return 0


# 숫자를 입력 받아 짝수인지 홀수인지 알려주는 함수를 만드세요
# 예) 3 => "홀수"
# 예) 10 =? "짝수"
n = input("숫자를 입력하세요:")
n = int(n)

def sub(n):
    if n%2 == 0 :
        return "짝수"
    else:
        return "홀수"

result1 = sub(10)
print(f' 결과:{result1}')
result2 = sub(3)
print(f' 결과:{result2}')

# 블록을 가지는 것 :함수,if,for
# 블록은 들여쓰기로 구분:space x tab o
# 블록은 변수의 scope

# a = 10 # 전역 변수
#   if a%2 == 0:
#     b = 5 # 지역 변수
#        print(b)

# print(a,b)

# for _ in range(10):
#     print(n) # 지역 변수

# def fun(x,y):
#     print(x,y) # 지역 변수

# fun(2,3)
# print(x,y) # 함수 블록 안에서 선언된 x,y는 지역 변수로
# 함수 밖에서는 사용 할 수 없다   

# 값을 하나 입력 받아 타입이 문자열이면 
# "문자입니다"를 출력하십쇼
def sub(dan):
    if type(dan) == str:
        return "문장입니다"
    else:
        return
result = sub('a')
print(result)

# 값을 하나 입력 받아 0보다 크면
# "양수입니다"를 출력하는 함수를 만드세요
def sub(n):
    if n > 0 :
        return "양수입니다"
    else:
        return 'x'
result = sub(10)
print(result)

# 리스트를 입력 받아 첫 번째 값을 반환하는 함수를 만드세요

def func(lis): # lis: 함수의 매개변수로 , 함수 내부에 선언함
    return lis[0] 

ml = [10,20,30] # my_lis: 함수에 전달하기 위한 리스트로, 메인에 선언함
result = func(ml) # result : 함수의 결과를 저장하기 위한 변수로 , 메인에 선언함
print(result)


        
# 문자열을 입력받아 길이를 반환하는 함수를 만드세요

def lis(cnt):
    if len(cnt):
        return  
result = lis("abc")
print(result)

# 문자열을 입력받아 길이 반환하는 함수 만들기
def func(msg): # msg 함수의 매개변수
    return len(msg)

my_str1 = "abc" # func 함수를 호출 할때 입력할 문자열
result1 = func(my_str1) # func 함수의 결과. "abc"의 길이를 저장할 변수
my_str2 = "hello"
result2 = func(my_str2)

# 숫자를 입력받아 양수,음수,0을 판별하는 함수를 만드세요
def func(n):
    if n > 0:
        return "양수"
    elif n < 0:
        return "음수"
    else :
        return "0"
func(5)
func(-3)
func(0)
result = func
print(result)

# 리스트를 입력 받아 리스트 안의 숫자를 모두 더해
# 합을 반환하는 함수를 만드세요
# 함수 정의 : 함수 이름, 입력값, 반환값

def func(a):
    sum = 0
    for num in a:
        sum = sum + num
    return sum

str1 = func(1,2,3,4,5)
print(str1)
str2 = func(10,20,30)  
print(str2)

# 단을 입력 받아 구구단을 출력하는 함수를 만드세요
# 예) 3 => 
def mul(lis):
    for n in range(1,10) :
        return (f"{lis} x {3} = {lis*3}")
mul(3)
