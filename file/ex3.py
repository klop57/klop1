# f = open('file2.txt' ,'w',encoding='utf-8')

# for i in range(1,11):
#     # i는 정수
#     # int => str
#     f.write(f'{i}번째 줄입니다\n')

# f.close()

# # file 입출력 문제
# # 'file2.txt'파일을 만들고 다음과 같이 쓰세요
# # "hello"
# # "hi"
# f = open('test.txt','w')
# f.write("hello\n")
# f.write("hi\n")
# f.close()


# # score.txt 파일을 만들고 다음과 같이 쓰세요
# # "80 90 70 100 60"

# f = open("score.txt", 'w')
# f.write("80 90 70 100 60")
# f.close()


# numbers.txt 파일을 만들고 다음과 같이 쓰세요
# 10부 20까지 출력
f = open('numbers.txt','w',encoding='utf-8')

for i in range(10,21):
    f.write(f'{i}\n')

f.close()


    