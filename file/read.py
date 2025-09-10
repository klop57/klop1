# 반대로 파일의 내용을 읽어오기

# 읽기모드로 파일 열기
# # 파일이름, 모드(w,r)
# f = open('새파일.txt','r')

# # 파일의 내용 읽어오기
# # 읽기 함수들 중에서
# # readlines는 결과를 리스트로 반환
# text = f.read()

# print(text)

# 사용이 끝났으면 닫기
# 문자열 안에 잇는 알파벳 하나씩 꺼내기
# 함수느의 인자: 구분자
# split 함수는 공백을 기주능로
# 문자열을 쪼개고 결과를 리스트로 반환
# text.split(' ')

# # for ch in lis:
# #     print(ch)

# # f.close()

# # 키보드에서 값 입력받기
# input()
# # 파일에서 값 읽어오기

# # 파일이름,모드
# f = open('file1.txt','r')

# # read 함수로 내용 읽어오기
# lis = f.readlines()

# for line in lis:
#     print(line,end ='')

# print('1', end ='\n')

# 파일 내용 읽어오기
# 파일이름, 모드
# 경로가 같으때는 파일 이름만 작성
# f = open('file2.txt','r',encoding='utf-8')

# # read 함수로 내용 읽기
# # readlines는 리스트로 반환
# lis = f.readlines()

# # 내용을 한줄씩 출력
# for line in lis:
#     print(line)

# 내용 추가 => 쓰기 모드 (w또는c)
# 'w'모드는 기존의 내용을 덮어씌움
# # 'a'모드는 이전 내용 뒤에 새로운 내용이 추가됨
# f = open('file2.txt','a',encoding='utf-8')

# for i in range(11,21):
#     f.write(f'{i}번째 줄입니다\n')

# f.close

# score.txt 파일을 읽고 
# 합계와 평균을 구하세요
# f = open ('score.txt','r')
# text = f.read()
# print(text)

# lis = text.split(' ')

# sum=0
# for s in lis:
#     sum = sum + int(s)
#     print(s,type(s))

# # cnt = len(lis)
# # print(sum/cnt)



# f = open('numbers.txt','r')
# lis = f.readlines()

# for line in lis:
#     if int(line)%2 == 0:
#         pass
#     print(type(line))
#     print(line, end='')

# f.close

# # 파일 쓰기 mode로 let's go~!
# f = open('new.txt','w')
# f.write('hello world')
# f.close()

# # 위 코드를 간단하게 작성하기
# # with를 사용하면 마지막에 자동으로 close가 실행됨
# with open('new.txt','w')as f: 
#     # 블록에는 수행하고 싶은 코드 작성
