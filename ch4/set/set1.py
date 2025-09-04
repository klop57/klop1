# set 만들기

s1 = {1,2,3}
print(s1,type(s1))
# 빈셋을 만들면 딕셔너리가 된다
s2 = {}
print(s2,type(s2))
# 형변환
# list => set
s3 = set([1,2,3])
print(s3)
# string => set
# 문자열의 문자들이 쪼개져서 set으로 저장됨
# set은 순서가 없다
s4 = set('string')
print(s4)