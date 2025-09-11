# 이전에 만든 기능 가져다 쓰기
# 모듈 만들기
import mod1

# 모듈에 있는 기능 사용하기
mod1.add(1,2)
mod1.sub(5,1)

# 모듈에서 특정함수만 가져오기
# from 모듈 import 함수
from mod1 import add

# 가져온 기능 사용하기
add(1,2)
# 이전에 썼던 코드
# mod1.add(1,2)x



# 모듈에 잇는  모든 함수 가지고 오기
#  *을 사용하면 하나씩 나열 할 필용벗음
from mod1 import *

add(1,2)
sum(2,1)





