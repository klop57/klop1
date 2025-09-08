
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
           
func(1,"apple",3.5,"banana",10,"hi")
func("a","b","c")
func(1,2,3)


        
   
