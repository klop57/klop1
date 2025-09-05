# 반복문을 사용해 1부터 10까지 출력
# i가 1부터 10까지 1씩 증가하면서
# 총 10번 반복 수행

i = 0
while i < 3:
    # 출력할 수는 1부터 10까지 변화하는 수
    print("반가워요")
    i += 1

i = 0
while i < 5:
    print((i+1)*2)
    i+=1
    
# 반복문 없이 3~6까지 출력
print(3)
print(4)
print(5)
print(6)

# 반복문으로 3~6까지 출력
i = 3
while i<7:
    print(i)
    i+=1


# 반복문으로 "hello"을 5번 출력
i = 0
while i < 5:
    print("hello")
    i+=1 

# 반복문으로 숫자 1~7까지 출력
i = 0
while i < 8:
    print(i)
    i+=1 


# 반복문으로 1 3 5 7 9 홀수 5개를 출력하세요

i = 1
while i <= 10:
    print(i)
    i+=2

# 또는

i = 0
while i < 5:
    print(i*2+1)
    i+=1     

# 반복문을 사용해서 11~20까지 출력
 
i=11
while i < 21:
    print(i)
    i+=1


# 반복문을 사용해서 11~20까지 합을 출력

 
i=11
sum=0 #합을 저장할 변수
while i < 21:
    print(i)
    i+=1

# 1+2+3+4+5
# 누적: 자기자신 + 더하는 수
sum = 0
sum = sum + 1
sum = sum + 2
sum = sum + 3
sum = sum + 4
sum = sum + 5

# i는 1부터 5까지 증가하는 수
i = 0
while i<6:
    # 더하는 수는 1~5
    sum = sum + i
    i+=1

# 반복문으로 리스트의
nums = [10,20,30]
print(nums[0])
print(nums[1])
print(nums[2])

# i는 0부터 2가 될떄까지
# 1씩 증가시키면서
# 총 3번 반복
i=0
while i < 3:
    # 인덱스는 0~2
    print(nums[i])
    i+=1

# 1~20까지 더한 합 구하기

i=1
sum=0
while i<=20:
    sum = sum+i
    i+=1

# 합이 100을 넘으면 반복문을 종료

i=1
sum=0

while i<=20:
    if sum > 100:
        break
    sum=sum+i
    i+=1

# 반복문으로 요소를 하나씩 출력하다가
# 77을 만나면 break를 사용해 반복문을 종료하세요.

lis = [100,77,-5,10]

i=0

while i < 4:
    if lis[i] == 77:
        break
    print(lis[i])    
    i+=1

# 1부터 10까지 하나씩 출력하다가
# 3의 배수를 만나면break를 사용해 반복문을 종료하세요
# print(9%5 == 0) #true

i=1
while i <= 10:
    if i%3 == 0:
        break
    print(i)
    i+=1

# 
lis = ['aa','bbb','cccc','dd']
i=0
while i < 4:
    if len(lis[i]) < 4:
        break 
    print (lis[i])
    i+=1

# 반복문으로 1부터 10까지 출력하세요
# 짝수는 건너뛰고 , 홀수만 출력하세요

i=1
while i <= 10:
    if i%2 == 0:
        i+=1
        continue
    print(i)
    i+=1

# 리스트 생성
lis = [10,'a',True,20,'b'] 

# while문으로 리스트의 요소를 하나씩 출력
# 단, 숫자를 만나면 continue를 사용해 건너뛰세요

i=0
while i < 5:
    if type(lis[i])== int:
        i+=1
        continue 
    print(lis[i])
    i+=1

print(type(10))
print(type('a'))
print(type(True))



    