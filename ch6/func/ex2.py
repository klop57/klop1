
# 단을 입력 받아 구구단을 출력하는 함수를 만드세요
# 예) 3 => 
def mul(lis):
    for n in range(1,10) :
        print(f"{lis} x {n} = {lis*n}")
mul(2)
mul(3)
mul(4)
mul(5)
mul(6)
mul(7)
mul(8)
mul(9)


# 2단부터 9까지 출력하세요

for i in range(2,10):
    print(i)
    mul(i)

# 리스트를 입력 받아 그 안에
# 문자열(str) 자료형이 몇개인지 세는 함수를 만드세요
# 예) [1,"apple",3.5,"banana",10,"hi"] => 3
# 예) ["a","b","c"] -> 3
# 예) [1,2,3] => 0

def func(n):
    for item in n:
        #  자료형은 '' 문자열 처리 x 예약어로 작성
        if type(item) == str :
            print(item, type(item)) # 1 int, 'apple' str
        # 조건 : if
        # 요소의 타입 == str


# 더하기 함수
def add(n1,n2):
    return n1+n2
# 함수 사용하기(호출하기)
# 사용 방법
# 함수이름 (필요한 값 입력)
result = add(3,4)
print(result)

# 함수 만들기
def func():
    pass

    func(1)

# 값을 두개 입력받고 호출하는 함수 만들기
def func2(a,b):
    print(a,b)

    func(1,2)

# 값을 세개 입력 받고 호출하는 함수 만들기
def func3(a,b,c):
    print(a,b,c)

func3(1,2,3)

# 매개변수의 개수가 달라져도
# 사용할 수 있는 함수 만들기           

# 나머지 매개변수
def func(**kwargs):
    print(kwargs)


# 함수 호출
    func(a=1)
    func(a=1,b=2)


# ------------------------------------------
# 딕셔너리의 함수 만들기
dic = {'name':"둘리",'age':10}
print(dic.keys())
print(dic.values())
print(dic.items())


# 나머지 매개변수를 사용하는 함수 만들기
# 사람의 정보를 입력받아 출력하는 함수 만들기
# 사람의 정보를 하나씩 꺼내기
def info(**kwargs):
    #item 객체에서 요소를 꺼내면 tuple
    #구조분해로 변수 두개에 key value 저장
    for key,value in kwargs.items():
        print(kwargs)
    

info(name="둘리", age=0)
info(name="도우너", age=8, address="서울")



dic = {'milk':2500,'bread':2000,'egg':3000}

def show_items(**kwargs):
    for food in kwargs.keys():
        print(food)

show_items(milk=2500,bread=2000,egg=3000)

# 두수의 차를 구하는 함수 정의
# 매개변수: 함수에 필요 입력값. 숫자 2개
# 반환값: 두 수의 차를 구해서 결과를 반환

def sub(n1,n2):
    return n1 - n2

result = sub(7,3)
print(result)


result = sub(n2=3,n1=7)
print(result)

# 문자열 두개를 입력받아 연결하는 함수 정의
def add_text(str1,str2):
    print(f'{str1}  {str2}')


# 함수 호출
add_text('hello','world')

add_text(str2 = 'world', str1 = 'hello')

# 문자를 입력 받고 나쁜말이 들어오면 종료하는 함수
def say_nick(nick):
    if nick == '바보':
        # return 키워드를 만나면
        # 더이상 코드를 실행하지 않고 함수를 종료됨
        # return 키워드 뒤에 값 생략 가능
        # 값이 return만 있으면 함수만 종료됨
        return
    print(f'나의 별명은{nick}입니다')
    

say_nick("짱구")
say_nick("바보")

def func():
    a = 1
    b = 2
    c = 3
    # 반환값은 무조건 1개
    return a, b, c

# return에 값을 여러개 쓰면 tuple로 묶어서 반환됨
print(func())

# 두 수를 입력 받아
# 첫번째 수를 두번째 수로 나누고 
# 몫을 출력하는 함수 만들기
# '나누는 수는 0이 될 수 없습니다'를 출력하고 
# 함수를 종료하세요
def divide(n1,n2):
    if n2 == 0:
        print("나누는 수는 0이 될 수 없습니다")
        return
    print (n1//n2)

divide(10,2)
divide(10,0)

def add(n1,n2):
    if type(n1) !=int or type(n2) !=int:
        print('입력받은 값이 숫자가 아닙니다')
        return
    print(f'{n1}+{n2}={n1+n2}')

add(3,4)
add(10,20)
add(5,'bb') # 문자를 입력하면 연결이 됩니다.
add('aa',5) # 문자를 입력하면 연결이 됩니다.
add('aa','bb') # 문자를 입력하면 연결이 됩니다.

# 나이를 입력받아 성인 여부를 출력하는 함수를 작성하세요
# 20 => 성인입니다
# 8 =>성인이 아닙니다
def func(age):
    if age < 0:
        print("잘못된 입력입니다")
        return
    if age >= 20:
        print("성인입니다")
    else:
        print("성인이 아닙니다")

func(20)
func(-5)

# 사람의 정보를 출력하는 함수 
# 매개변수: 이름,나이,성별
# 성별의 초기값 설정
def info(name,gender,age):
    print(f'나의 이름은 {name}입니다')
    print(f'나의 나이은 {age}입니다')
    if gender == 'm':
        print("남자입니다")
    else:
        print("여자입니다")

# 매개변수의 개수가 맞지 않으면 함수 호출 안됨
info('도우너',8,'m')
info('둘리',10,'f')

# 변수
# 전역, 지역을 나누는 이유: 
# scope(유효범휘)를 파악하여 사용할 수 있는 범위를 확인하기 위해

a=1 # 전역 변수 (어디서든 사용가능)

def func(a): # 지역 변수 (함수 내부에서만 사용 가능)
    a = a + 1

func(a)
print(a)

def func(b):
    b = 3
    print(b)

def add(a,b):
    return a + b
# 람다 함수 생성
# 변수 = lambda 매개변수:반환값
# 변수 = 함수
add = lambda a,b : a+b

# 람다 함수 호출
sum = 0
result = add(3,4)
print(result)

# 복합 대입, 람다함수는 선택
sum += 1

# 문장열 정렬
strings = ['foo','card','ba','aaa']

# short는 원본을 변경하는 함수
# 반환x
# 숫자는 자동으로 오름차순
# 하지만 문자는 정렬기준이 없으므로
# 람다함수는 정렬기준을 작성해야함
strings.sort( key = lambda x : len(x))
print(strings)






   
