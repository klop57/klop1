# 클래스 이름은 대문자로 시작
class Sample:
    pass
# 클래스 사용하기
# 변수 =클래스이름()
a = Sample()
b = Sample()

# 학생 클래스 만들기

# 현실에서 존재하는 학생이라는 객체를
# 프로그램에서 관리하기 위해 클래스를 설계하는 것

# 학생이 가지고 있는 데이터와 기능을 클래스로 표현

class Student:
    # self 매개변수
    # self는 특별한 변수로,함수 호출시 자동으로 생성됨
    # self에는 자기자신 .함수를 포함하고 잇는 클래스가 들어감
    def setdata(self,id,name,grade): #학번,이름,학년 저장하는 함수
        self.student_id = id
        self.student_name = name
        self.student_grade = grade

    def info(self):  # 학생의 정보를 출력하는 함수
        print(f'저는 {self.student_grade}학년 {self.student_name}입니다')

# 클래스 사용하기
stu1 = Student()
# 클래스로 객체를 생성하고
# 객체의 함수를 사용
stu1 =Student()
stu1.setdata(101,'둘리',2)
stu1.info()

# 두번째 학생을 만들고 학생의 정보를 초기화
stu2 = Student()
stu2.setdata(102,'도우너',2)
stu1.info()

# 세번째 학생을 만들고 학생의 정보를 초기화 
stu1 =Student()
stu1.setdata(103,'또치',2)
stu1.info()



# ------------복습--------------------------------------------------------

class Student:
    def __init__(self,id,name,grade):
        self.stu_id = id
        self.stu_name = name
        self.stu_grade = grade

    def info(self):
        print(f'학번:{self.stu_grade},이름:{self.stu_name}')

# 가나다라마바사아자차카
stu1 = Student(101,'둘리',2)
stu1.info()

stu2 = Student(102,'도우너',2)
print(stu2.stu_id)
print(stu2.stu_name)
print(stu2.stu_grade)


# 도서정보를 저장하기 위한 클래스 만들기

class Book:
    def __init__(self,title,author,price):
        self.book_title = title
        self.book_author = author
        self.book_price = price

    def info(self):
        print(f'제목: {self.book_title}, 가격: {self.book_price}, 저자: {self.book_author}')

book1 = Book("데미안","김동현",13000)
book1.info()
book2 = Book("그대는 등신이다","알렉산더 2세",200)
book2.info()
book3 = Book("혁명적인 그대에게","레오나르도 다비침",19000)
book3.info()


# 자동차 객체를 2대 만들고 정보를 출력하세요
# 소나타 흰색 
# 아반떼 검정

class Car:
    def __init__(self,model,color):
        self.car_model = model
        self.car_color = color
    def info(self):
        print(f'모델: {self.car_model}, 색상: {self.car_color}')

car1= Car("소나터","white")
car1.info()
car2= Car("아반떼","black")
car2.info()

# order 클래스를 만들어주세요
# 속성: 주문번호, 상품명, 수량
# 기능: 주문번호화 상품명 출력
# order 클래스로 객체를 2개 만들고 출력하세요
# )실행결과
# 101 노트북 3
# 102 마우스 5



class order:
    def __init__(self,order_numder,product_name,quantity):
        self.order_numder = order_numder
        self.product_name = product_name
        self.quantity = quantity

    def info(self):
        print(self.order_numder, self.product_name, self.quantity)

# 객체 생성
obj1 = order(101, "노트북", 3)
obj1.info()
obj2 = order(102, "마우스", 5)
obj2.info()

# 커피 클래스

class Coffee:
    def __init__(self,name):
        self.coffee_name = name
        self.cnt = 0
    def order(self,num):
        self.cnt = self.cnt + num
        print(f'{self.coffee_name}를(을){num}잔을 추가 주문했습니다')
        print(f'총{self.cnt}잔')

c1 = Coffee('아메리카노')
c2 = Coffee('라떼')
c1.order(2)
c1.order(3)
c2.order(48)
c2.order(1241248)

# 버스
class Bus:
    def __init__(self,bus_number):
        self.bus_number = bus_number
        self.cnt = 0
    def info(self,num):
        self.cnt = self.cnt + num
        print(f'{self.bus_number}버스에 {num}승객이 탑승했습니다')
        print(f'총{self.cnt}명의 승객이 탑승했습니다')    

p1 = Bus(9)
p2 = Bus(111)
p1.info(10)
p1.info(5)
p2.info(3)
p2.info(6)

# subway 클래스

class Subway:
    def __init__(self,line,fare=1500):
        self.subway_line = line
        self.passenger= 0
        self.fare = fare
        self.fare = 0
    def take(self,num,cnt):
        print(f'{self.subway_line} 호선에 승객{num}이 탑승햇습니다')
        print(f'총 {self.passenger}명이 탑승했습니다')
        print(f'총 {self.fare}원 입니다')

s1 = Subway('2호선')
s2 = Subway('9호선')


# 예금 클라스를 만드세요
# 속성 : 잔액
# 기능 : 입금하기 / 출금하기
# 단, 출금시 예금이 부족하면 "잔액이 부족합니다"를 출력

# 실행 결과:
# 10000원 입금 완료. 현재 잔액 : 10000원
# 3000원 출금 완료. 현재 잔액  : 7000원
# 잔액이 부족합니다.

class Account:   
    # 입금: deposit 출금: withdraw
    def __init__(self):
        self.balance = 0

    def deposit(self, money):
        self.balance = self.balance + money
        print(f"{money}원 입금 완료. 현재 잔액 : {self.balance}원")

    def withdraw(self, money):
        if money > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance = self.balance - money
            print(f"{money}원 출금 완료. 현재 잔액 : {self.balance}원")

# 실행 예시
acc = Account()
acc.deposit(10000)
acc.withdraw(3000)
acc.withdraw(8000)


# 사람 클래스 만들기
class Person:
    def eat(self):
        print('밥을 먹는다')
    def sleep(self):
        print('잠을 잔다')
 
class Student(Person):
    def study(self):
        print("학생은 공부를 한다")

s = Student()
s.eat()
s.sleep()
s.study()

# 또 다른 자식 클래스 
class Teacher(Person):
    def teach(self):
        print('학생들을 가르친다')


t = Teacher()
t.eat()
t.sleep()
t.teach()



class Animal:
    def eat(self):
        print("동물이 먹습니다")

a = Animal()
a.eat()

class Dog(Animal):
    def bark(self):
        print ("강아지가 짖습니다")

d= Dog()
d.eat()
d.bark()

# =------------------
class Book:
    def read(self):
        print('책을 읽습니다')
d = Book()
d.read()

class Ebook(Book):
    def download(self):
        print('전자책을 다운로드 받습니다')

eb = Ebook()
eb.download()

# --------------------

class Monster:
    def attack(self):
        print('몬스터가 기본 공격을 합니다!')
m = Monster()
m.attack()

class Slime(Monster):
    def jump_attack(self):
        print('슬라임이 점프해서 몸통 박치기를 합니다')

s = Slime()
s.jump_attack()

# ----------------------

class Animal:
    def bark(self):
        print('동물이 소리를 낸다')
        
class Dog(Animal):
     def bark(self):
        print("멍멍멍")

d = Dog()
d.bark()

class Cat(Animal):
      def bark(self):
         print("냐옹")

c = Cat()
c.bark() 

class Student:
    
    school = '연희직업전문학교'

    def __init__(self,id,name):
        self.student_id = id
        self.student_name = name
        self.school = '연희직업전문학교'
    def info(self):
        print(f'이름: {self.student_name} , 학교: {self.school}')
# 학생 2명 만들기
# 객체 생성시 무조건 학생의 정보를 입력해야함
s1 = Student(101,'둘리')
s1.info()
s2 = Student(102,'도우너')
s2.info()

# 클래스
Student.school = '파이썬 학교'

s1.info()
s2.info()



# 멤버변수로 school을 넣엇을때
# 모든 객체가 똑같은 데이터를 가짐 => 메모리 낭비

# 클래스 뵨수로 school을 넣었을때
# 메모리에 딱 한번만 '연희직업전문학교'가 저장되고
# 모든 객체가 클래스 변수를 공유함

# 정리:
# 클래스 변수 - 모든 객체가 공유하는 데이터
# 인스턴스 변수 - 객체 고유의 데이터
