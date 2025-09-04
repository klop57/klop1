# 1 객체 비교하기 (is ==)

a = [1,2,3]
# a를 복사
b = a
c = [1,2,3]

# is 연산자로 두 변수가 같은지 비교

# is : 두 변수가 같은 객체를 가르키는 것
print(a is b)
print(a is not b)
# == : 두 변수가 같은 내용을 가지고 있는지
print( a == b)
print( a == c)