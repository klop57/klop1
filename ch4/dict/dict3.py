# 딕셔너리 관련 함수

dic = {'name': '둘리','age':20,'address': '인천'}

# 리스트와 비슷하게 생겼지만 dict_keys라는 객체
print(dic.keys())
print(type(dic.keys()))
# dict_keys(['name','phone','birth'])
# <class 'dict_keys'>

# 값 목록 조회
print(dic.values())
# dict_values(['둘리',20,'인천'])

# 모든 데이터 조회
print(dic.items()) # dict_items([('name', '둘리'), ('age', 20), ('address', '인천')])

# 값 꺼내기
print(dic['name'])
print(dic.get('age'))

# 특정키가 포함되어 있는지 확인
print('name' in dic)
print('aaa' in dic)


