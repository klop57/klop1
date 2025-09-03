# 1 객체 비교하기 (is ==)

a = [1,2,3]
# a를 복사
b = a
c = [1,2,3]
# is 연산자로 두 변수가 같은지 비교
print(a is b)
print(a is not b)
print( a == b)
print( a == c)